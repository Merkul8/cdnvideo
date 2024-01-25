from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Город')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    