# Generated by Django 5.1 on 2024-09-04 07:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('current_temperature', models.FloatField()),
                ('current_humidity', models.FloatField()),
                ('current_pressure', models.IntegerField()),
                ('current_wind_speed', models.FloatField()),
                ('current_uv_index', models.FloatField()),
                ('current_weather_text', models.CharField(max_length=100)),
                ('current_weather_icon_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_location', models.CharField(default='Gothenburg', max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
