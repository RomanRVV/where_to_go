from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name='Заголовок')
    description_short = models.TextField(blank=True, verbose_name='Короткое описание')
    description_long = models.TextField(blank=True, verbose_name='Длинное описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


