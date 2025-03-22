from rest_framework import generics
from .models import AgriTechSensorData, MedTechSensorData, FinTechSensorData, OtherSensorData
from .serializers import SensorDataSerializer

class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = AgriTechSensorData.objects.all()
    serializer_class = SensorDataSerializer

class SensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgriTechSensorData.objects.all()
    serializer_class = SensorDataSerializer

class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = MedTechSensorData.objects.all()
    serializer_class = SensorDataSerializer

class SensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedTechSensorData.objects.all()
    serializer_class = SensorDataSerializer

class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = FinTechSensorData.objects.all()
    serializer_class = SensorDataSerializer

class SensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinTechSensorData.objects.all()
    serializer_class = SensorDataSerializer

class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = OtherSensorData.objects.all()
    serializer_class = SensorDataSerializer

class SensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OtherSensorData.objects.all()
    serializer_class = SensorDataSerializer