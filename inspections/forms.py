from ajaximage import fields
from django import forms
from django.db import transaction
from core.forms import BaseLoginForm, ErrorsOnFirstFieldMixin
from vehicles.models import Vehicle
from .models import Inspection, InspectionCode
from django.utils.html import format_html, mark_safe, force_text
from itertools import chain

__all__ = ["MechanicLoginForm", "InspectionForm", "InitialForm", "VehicleForm", "PhotoForm"]


class MechanicLoginForm(ErrorsOnFirstFieldMixin, BaseLoginForm):

    def confirm_login_allowed(self, user):
        super(MechanicLoginForm, self).confirm_login_allowed(user)

        if (user.is_superuser):
            return

        # Prevent all users lacking a group that has been assigned to a shop from logging in
        shop_permissions = user.groups.exclude(shop__id__isnull=True).count()

        if (shop_permissions == 0):
            raise forms.ValidationError(self.error_messages['invalid_login'])

class InitialForm(ErrorsOnFirstFieldMixin, forms.ModelForm):
    shops = None
    code = None
    creating = True

    def __init__(self, *args, **kwargs):
        self.shops = kwargs.pop('shops', [])

        super(InitialForm, self).__init__(*args, **kwargs)

        if len(self.shops) == 1:
            self.fields.pop('shop')

    def clean_id(self):
        """
        Validate that a matching inspection code exists for this form,
        or that the inspection exists.
        """
        # If the instance already exists then disregard this step
        if self.instance.pk:
            return self.instance.pk

        id = self.cleaned_data.get("id")

        # Otherwise check if the inspection code exists
        code = InspectionCode.objects.filter(id=id).first()

        if code is None:
            raise forms.ValidationError('No matching inspection code found.')
            return id
        elif code.is_redeemed:
            raise forms.ValidationError('This inspection code has already been redeemed.')
            return id

        self.code = code
        return id


    @transaction.atomic
    def save(self, *args, **kwargs):
        kwargs.update({ "commit" : False })
        instance = super(InitialForm, self).save(*args, **kwargs)

        if not self.instance.pk:
            if not self.code.is_redeemed:
                self.code.is_redeemed = True
                self.code.save()

            kwargs.update({'commit' : False})

            # If the shop isn't set through the form
            # it means the field was excluded and we should set it to the techs first shop
            if instance.shop_id is None:
                instance.shop_id = self.shops[0].id

            # set the inspection customer to the user who provided the code
            instance.customer = self.code.user

        instance.save()

    class Meta:
        model = Inspection
        fields = ('id', 'shop')


class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.inspection = kwargs.pop('inspection')
        super(VehicleForm, self).__init__(*args, **kwargs);

    class Meta:
        model = Vehicle
        fields = ('vin', 'car_model', 'body', 'transmission',
                  'fuel_type', 'colour', 'mileage', 'year')

    def save(self, *args, **kwargs):
        # include shop and user id here
        kwargs.update({ "commit" : False })
        instance = super(VehicleForm, self).save(*args, **kwargs)

        if self.instance.pk:
            instance.save()
            return instance

        instance.owner = self.inspection.customer
        return instance

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Inspection
        fields = ('image_front', 'image_drivers_side', 'image_passengers_side', 'image_back',
                  'image_dash', 'image_interior')

class InspectionForm(forms.ModelForm):

    inspection_id = forms.CharField(max_length=10, required=True)
    images = forms.URLField(widget=fields.AjaxImageWidget(upload_to='form-uploads'))

    def save(self, *args, **kwargs):
        # include shop and user id here
        self.vehicle_form.save(*args, **kwargs)
        return super(InspectionForm, self).save(*args, **kwargs)

    class Meta:
        model = Inspection
        widgets = {
            'name': forms.RadioSelect(),
        }
        exclude = ('id', 'customer', 'shop', 'vehicle')