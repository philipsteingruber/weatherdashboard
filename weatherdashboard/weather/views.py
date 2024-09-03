from datetime import datetime as dt

import pytz
import requests
from django.shortcuts import render
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

from .constants import API_KEY

tf = TimezoneFinder()
geolocator = Nominatim(user_agent="weatherdashboard")


def get_local_time(city: str):
    location = geolocator.geocode(city)
    tz = pytz.timezone(tf.timezone_at(lng=location.longitude, lat=location.latitude))
    return dt.now(tz=tz).time().strftime("%H:%M")


def get_weather(city: str):
    query_url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no'
    response = requests.get(query_url)
    return response.json()


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
    current_time = get_local_time(city)
    country = get_country(city)

    context = {'weather_data': weather_data, 'city': city.title(), 'current_time': current_time, 'country': country}
    return render(request, 'weather/layout.html', context=context)
