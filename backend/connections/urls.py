from rest_framework.routers import DefaultRouter
from .views import DataConnectionViewSet
router = DefaultRouter()
router.register('', DataConnectionViewSet)
urlpatterns = router.urls
