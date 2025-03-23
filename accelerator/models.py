from django.db import models
from django.forms import JSONField

class BaseSensorData(models.Model):
    INDUSTRY_CHOICES = [
        ('AgriTech', 'AgriTech'),
        ('MedTech','MedTech'),
        ('FinTech','FinTech'),
        ('Other', 'Other'),

    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    industry_type = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    sensor_type = models.CharField(max_length=50,)
    image = models.ImageField(upload_to='data_images/', null=True, blank=True)
    class Meta:
        abstract = True
    def __str__(self):
        return f"{self.industry_type} -{self.sensor_type} - {self.image} - {self.timestamp}"

class AgriTechSensorData(BaseSensorData):
    sensor_id = models.IntegerField(null=True, blank=True)
    soil_moisture = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    light_intensity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"AgriSensor: {self.sensor_id} - Soil Moisture: {self.soil_moisture}%"

class MedTechSensorData(BaseSensorData):
    patient_id = models.IntegerField(null=True, blank=True)
    heart_rate = models.IntegerField(null=True, blank=True)
    blood_pressure = models.CharField(max_length=10, null=True, blank=True)
    body_temperature = models.FloatField(null=True, blank=True)
    oxygen_level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Patient: {self.patient_id} - Heart Rate: {self.heart_rate} bpm"

class FinTechSensorData(BaseSensorData):
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    account_id = models.CharField(max_length=100, null=True, blank=True)
    transaction_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    transaction_type = models.CharField(max_length=50, null=True, blank=True)
    stock_symbol = models.CharField(max_length=10, null=True, blank=True)
    stock_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"FinTech: {self.transaction_id} - Amount: N{self.transaction_amount}"

class OtherSensorData(BaseSensorData):
    def __str__(self):
        return f"Others:  {self.sensor_type}"

