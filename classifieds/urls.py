from rest_framework import routers

from .views import ClassifiedViewSet

router = routers.DefaultRouter()
router.register('classifieds', ClassifiedViewSet)

urlpatterns = router.urls
