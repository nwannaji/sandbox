from django import forms
from .models import AgriTechSensorData, MedTechSensorData, FinTechSensorData, OtherSensorData

class AgricTechSensorDataForm(forms.ModelForm):
    class Meta:
        model = AgriTechSensorData
        fields = '__all__'
        widgets = {
            'timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class MedTechSensorDataForm(forms.ModelForm):
    class Meta:
        model = MedTechSensorData
        fields = '__all__'
        widgets = {
            'timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class FinTechSensorDataForm(forms.ModelForm):
    class Meta:
        model = FinTechSensorData
        fields = '__all__'
        widgets = {
            'timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class OtherSensorDataForm(forms.ModelForm):
    class Meta:
        model = OtherSensorData
        fields = '__all__'
        widgets = {
            'timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }