from rest_framework import serializers
from .models import DataConnection
class DataConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataConnection
        fields = '__all__'
