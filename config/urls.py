from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import core.views

urlpatterns = [
    url(r'^ajaximage/', include('ajaximage.urls')),
    url(r'inspections/', include('inspections.urls', namespace='inspections')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core.views.HomePageView.as_view(), name='home'),
    url(r'^search/$', core.views.SearchView.as_view(), name='search'),
    url(r'^profile/$', core.views.ProfileView.as_view(), name='profile'),
    url(r'^details/$', core.views.DetailView.as_view(), name='details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
