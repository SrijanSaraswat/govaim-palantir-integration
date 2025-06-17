from rest_framework import viewsets
from .models import DataConnection
from .serializers import DataConnectionSerializer
class DataConnectionViewSet(viewsets.ModelViewSet):
    queryset = DataConnection.objects.all()
    serializer_class = DataConnectionSerializer
