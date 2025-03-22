from rest_framework import serializers
from .models import AgriTechSensorData, MedTechSensorData,FinTechSensorData,OtherSensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriTechSensorData
        fields = '__all__'

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedTechSensorData
        fields = '__all__'

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinTechSensorData
        fields = '__all__'

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherSensorData
        fields = '__all__'
