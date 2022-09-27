from rest_framework import serializers
from .models import SensorData

class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['sensor_id', 'timestamp', 'sensor_type', 'reading']

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    class Meta:
        fields = ['file']
