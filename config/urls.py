from django.conf.urls import include, url
from django.contrib import admin

import core.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core.views.HomePageView.as_view(), name='home'),
    url(r'^search/$', core.views.SearchView.as_view(), name='search'),
    url(r'', include('classifieds.urls', namespace='classifieds'))
]
