from django.conf.urls import include, url
from django.contrib import admin

import core.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core.views.HomePageView.as_view(), name='home'),
    url(r'^search/$', core.views.SearchView.as_view(), name='search'),
    url(r'^profile/$', core.views.ProfileView.as_view(), name='profile'),
    url(r'^details/$', core.views.DetailView.as_view(), name='details'),
]
