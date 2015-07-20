from django.conf.urls import url
import inspections.views

urlpatterns = [
    url(r'^login/$', inspections.views.InspectionLoginView.as_view(), name='login'),
    url(r'^list/$', inspections.views.InspectionListView.as_view(), name='list'),
    url(r'^form/$', inspections.views.InspectionFormView.as_view(), name='form'),
]
