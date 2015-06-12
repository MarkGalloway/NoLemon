from rest_framework import routers

from .views import AdvertisementViewSet

router = routers.SimpleRouter()
router.register('advertisements', AdvertisementViewSet)

urlpatterns = router.urls
