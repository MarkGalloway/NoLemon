from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^login/$', InspectionLoginView.as_view(), name='login'),
    url(r'^logout/$', InspectionLogoutView.as_view(), name='logout'),
    url(r'^list/$', InspectionListView.as_view(), name='list'),
    url(r'^form/(?P<id>[0-9a-zA-Z]{6, 15})/$', InitialView.as_view(), name='existing-form'),
    url(r'^test/$', Test.as_view(), name='test'),

    url(r'^form/$', InitialView.as_view(), name='form'),
    url(r'^/initial-ajax/$', InitialAjax.as_view(), name='initial_ajax'),

    url(r'^vehicles/$', VehicleFormView.as_view(), name='vehicles'),
    url(r'^vehicles/(?P<id>\w+)/$', VehicleFormView.as_view(), name='vehicles'),
    url(r'^/vehicle-ajax/(?P<id>\w+)/$', VehicleAjax.as_view(), name='vehicle_ajax'),

    url(r'^photos/(?P<id>\w+)/$', PhotosFormView.as_view(), name='photos'),
    url(r'^/photos-ajax/(?P<id>\w+)/$', PhotosAjax.as_view(), name='photos_ajax'),
]

