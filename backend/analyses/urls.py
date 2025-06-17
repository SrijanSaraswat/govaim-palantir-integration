from rest_framework.routers import DefaultRouter
from .views import AnalysisViewSet
router = DefaultRouter()
router.register('', AnalysisViewSet)
urlpatterns = router.urls
