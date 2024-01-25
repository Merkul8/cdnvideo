from django.db import models


class City(models.Model):
    """ Модель города с данными о широте и долготе """
    name = models.CharField(max_length=255, verbose_name='Город')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name