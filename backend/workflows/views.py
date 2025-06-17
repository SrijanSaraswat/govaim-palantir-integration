from rest_framework import viewsets
from .models import Workflow
from .serializers import WorkflowSerializer
class WorkflowViewSet(viewsets.ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer
