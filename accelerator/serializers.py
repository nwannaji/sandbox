from rest_framework import serializers
from .models import AgriTechSensorData, MedTechSensorData, FinTechSensorData, OtherSensorData

class AgriTechSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriTechSensorData
        fields = '__all__'

class MedTechSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedTechSensorData
        fields = '__all__'

class FinTechSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinTechSensorData
        fields = '__all__'

class OtherSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherSensorData
        fields = '__all__'
