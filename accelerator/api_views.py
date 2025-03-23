from rest_framework import generics
from .models import AgriTechSensorData, MedTechSensorData, FinTechSensorData, OtherSensorData
from .serializers import AgriTechSensorDataSerializer, MedTechSensorDataSerializer, FinTechSensorDataSerializer, OtherSensorDataSerializer

# AgriTech API Views
class AgriTechSensorDataListCreateView(generics.ListCreateAPIView):
    queryset = AgriTechSensorData.objects.all()
    serializer_class = AgriTechSensorDataSerializer

class AgriTechSensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgriTechSensorData.objects.all()
    serializer_class = AgriTechSensorDataSerializer

# MedTech API Views
class MedTechSensorDataListCreateView(generics.ListCreateAPIView):
    queryset = MedTechSensorData.objects.all()
    serializer_class = MedTechSensorDataSerializer

class MedTechSensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedTechSensorData.objects.all()
    serializer_class = MedTechSensorDataSerializer

# FinTech API Views
class FinTechSensorDataListCreateView(generics.ListCreateAPIView):
    queryset = FinTechSensorData.objects.all()
    serializer_class = FinTechSensorDataSerializer

class FinTechSensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinTechSensorData.objects.all()
    serializer_class = FinTechSensorDataSerializer

# Other Sensor API Views
class OtherSensorDataListCreateView(generics.ListCreateAPIView):
    queryset = OtherSensorData.objects.all()
    serializer_class = OtherSensorDataSerializer

class OtherSensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OtherSensorData.objects.all()
    serializer_class = OtherSensorDataSerializer
