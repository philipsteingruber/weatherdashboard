from datetime import datetime as dt

import pytz
import requests
from django.shortcuts import render
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from .models import WeatherData

from .constants import API_KEY
from geopy.exc import GeocoderUnavailable, GeopyError

tf = TimezoneFinder()
geolocator = Nominatim(user_agent="weatherdashboard")


def get_local_time(city: str):
    location = geolocator.geocode(city)
    tz = pytz.timezone(tf.timezone_at(lng=location.longitude, lat=location.latitude))
    return dt.now(tz=tz).time().strftime("%H:%M")


def get_weather(city: str):
    query_url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no'
    data = requests.get(query_url).json()['current']

    weather = WeatherData.objects.create()
    weather.city = city
    weather.current_temperature = data['temp_c']
    weather.current_feelslike = data['feelslike_c']
    weather.current_humidity = data['humidity']
    weather.current_pressure = int(data['pressure_mb'])
    weather.current_wind_speed = round(data['wind_kph'] / 3.6, 1) # Convert to m/s
    weather.current_uv_index = data['uv']
    weather.current_weather_text = data['condition']['text']
    weather.current_weather_icon_url = data['condition']['icon']
    weather.save()

    return weather


def get_country(city: str):
    location = geolocator.geocode(city)
    return str(location).split(',')[-1].strip().title()


def index(request):
    city = request.GET.get('q')
    if not city:
        city = 'Gothenburg'

    try:
        geolocator.geocode(city).longitude
    except AttributeError:
        city = 'Gothenburg'

    weather_data = get_weather(city)
    try:
        current_time = get_local_time(city)
        country = get_country(city)
    except GeopyError:
        current_time = dt.now().time().strftime("%H:%M")
        country = 'Sweden'
        print('Geocoder failed, setting defaults')

    context = {'weather_data': weather_data, 'city': city.title(), 'current_time': current_time, 'country': country}
    return render(request, 'weather/layout.html', context=context)
