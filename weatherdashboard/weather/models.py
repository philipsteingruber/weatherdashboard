from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class WeatherData(models.Model):
    city = models.CharField(max_length=50, null=False, blank=False)
    current_temperature = models.FloatField(null=True, blank=True)
    current_feelslike = models.FloatField(null=True, blank=True)
    current_humidity = models.FloatField(null=True, blank=True)
    current_pressure = models.IntegerField(null=True, blank=True)
    current_wind_speed = models.FloatField(null=True, blank=True)
    current_uv_index = models.FloatField(null=True, blank=True)
    current_weather_text = models.CharField(max_length=100, null=False, blank=False)
    current_weather_icon_url = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f'{self.city}, {self.current_temperature}, {self.current_humidity}, {self.current_wind_speed}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_location = models.CharField(max_length=50, null=False, blank=False, default='Gothenburg')
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
