from django.db import models
from core.models import TimeStampedModel


class Location(TimeStampedModel):
    name = models.CharField('Name', max_length=255)
    longitude = models.CharField('Longitude', blank=True, max_length=128)
    latitude = models.CharField('Latitude', blank=True, max_length=128)
    address = models.CharField('Latitude', blank=True, max_length=255)
    city = models.CharField('Latitude', blank=True, max_length=64)
    state = models.CharField('Latitude', blank=True, max_length=2)
    postal_code = models.CharField('Latitude', blank=True, max_length=10)
