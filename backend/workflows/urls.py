from rest_framework.routers import DefaultRouter
from .views import WorkflowViewSet
router = DefaultRouter()
router.register('', WorkflowViewSet)
urlpatterns = router.urls
