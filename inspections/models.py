import time
import datetime
from hashids import Hashids
from django.db import models
from django.db import IntegrityError
from django import forms
from django.contrib.auth.models import Group
from core.models import phone_validator
from django import forms
from django.utils.html import conditional_escape, format_html
from ajaximage.fields import AjaxImageField

__all__ = ['Inspection', 'Shop', 'InspectionCode']

hashids = Hashids('23456789ABCDEFGHIJKLMNPQRSTUVQXYZabdefghijpqrtqy')


def generate_referral_code():
    # encode the timestamp in nano seconds
    return hashids.encode(int(time.time() * 1000))

class Shop(models.Model):
    """
    A model representing a mechanic shop
    """

    name = models.CharField(max_length=70)
    group = models.OneToOneField(Group, null=True, blank=True)
    phone = models.CharField(max_length=15, default="", blank=True, validators=[phone_validator])
    address = models.ForeignKey('core.Address')

    def __str__(self):
        return self.name


class CustomRadioChoiceInput(forms.widgets.RadioChoiceInput):
    input_type = 'radio'

    def render(self, name=None, value=None, attrs=None, choices=()):
        if self.id_for_label:
            label_for = format_html(' for="{}"', self.id_for_label)
        else:
            label_for = ''
        attrs = dict(self.attrs, **attrs) if attrs else self.attrs
        return format_html(
            '{}<label{} class="{}"></label>', self.tag(attrs), label_for, self.choice_label
        )


class CustomRadioFieldRenderer(forms.widgets.RadioFieldRenderer):
    choice_input_class = CustomRadioChoiceInput
    outer_html = '{content}'
    inner_html = '{choice_value}{sub_widgets}'


class CustomRadioSelect(forms.RadioSelect):
    renderer = CustomRadioFieldRenderer


class RadioModelChoiceField(forms.TypedChoiceField):
    widget = CustomRadioSelect


class RadioSmallIntegerField(models.PositiveSmallIntegerField):
        def formfield(self, *args, **kwargs):
            defaults = {'choices_form_class': RadioModelChoiceField}
            defaults.update(kwargs)
            return super(RadioSmallIntegerField, self).formfield(**defaults)

class Inspection(models.Model):
    """
    A model representing a No Lemon inspection
    """
    id = models.CharField(max_length=10, primary_key=True)
    customer = models.ForeignKey('core.User', related_name="inspections")
    shop = models.ForeignKey('Shop', verbose_name='Technician Shop', related_name="inspections")
    vehicle = models.ForeignKey('vehicles.Vehicle', related_name="inspections", null=True)
    date_completed = models.DateTimeField(blank=True, null=True)

    image_front = AjaxImageField(upload_to='inspection-uploads', null=True, blank=True)
    image_drivers_side = AjaxImageField(upload_to='inspection-uploads', blank=True)
    image_passengers_side = AjaxImageField(upload_to='inspection-uploads', blank=True)
    image_back = AjaxImageField(upload_to='inspection-uploads', blank=True)
    image_dash = AjaxImageField(upload_to='inspection-uploads', blank=True)
    image_interior = AjaxImageField(upload_to='inspection-uploads', blank=True)

    CHOICES = [(1,'Good'), (2,'Fair'), (3, 'Poor')]
    CHOICES_OPTIONAL = [(0,'Not-Applicable')] + CHOICES

    # Exterior
    windshield = RadioSmallIntegerField(choices=CHOICES, default=3, null=True)
    wipers = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)
    windows = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)
    mirrors = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)
    exterior_condition = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)

    # Lights
    headlights = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)
    fog_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)
    signal_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)
    hazard_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)
    backup_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)
    dome_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3, null=True)

    trunk_light = models.PositiveSmallIntegerField(choices=CHOICES_OPTIONAL, default=3, null=True)
    license_light = models.PositiveSmallIntegerField(choices=CHOICES_OPTIONAL, default=3, null=True)

    exterior_notes = models.TextField('Notes', blank=True, default="", null=True)
    technician = models.CharField(max_length=70, null=True)

    def __str__(self):
        return self.id


class InspectionCode(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=generate_referral_code)
    user = models.ForeignKey('core.User', related_name="inspection_codes")
    is_redeemed =  models.BooleanField('Redeemed', default=False)
    redeemed_on =  models.DateField('Redeemed On', null=True)

    def save(self, *args, **kwargs):
        if (self.is_redeemed and not self.redeemed_on):
            self.redeemed_on = datetime.datetime.today()
        elif (not self.is_redeemed and self.redeemed_on):
            self.redeemed_on = None

        unique = False
        while not unique:
            try:
                super(InspectionCode, self).save(*args, **kwargs)
            except IntegrityError:
                self.code = generate_referral_code()
            else:
                unique = True

        def __str__(self):
            return self.id