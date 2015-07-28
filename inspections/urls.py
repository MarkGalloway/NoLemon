from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', InspectionLoginView.as_view(), name='login'),
    url(r'^logout/$', InspectionLogoutView.as_view(), name='logout'),
    url(r'^list/$', InspectionListView.as_view(), name='list'),
    url(r'^form/$', InspectionFormView.as_view(), name='form'),
]
