from django.db import models

class SensorData(models.Model):
    sensor_id = models.IntegerField()
    timestamp = models.DateTimeField()
    sensor_type = models.CharField(max_length=30)
    reading = models.IntegerField()
