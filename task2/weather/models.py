from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=100, unique=True)
    temperature = models.IntegerField()
    atmosphere_pressure = models.IntegerField()
    wind_speed = models.IntegerField()
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city
