from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    short_description = models.TextField(blank=True, verbose_name='Короткое описание')
    long_description = HTMLField(blank=True, verbose_name='Длинное описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class PlacesImage(models.Model):
    position = models.PositiveIntegerField(default=0,
                                           blank=False,
                                           null=False,
                                           verbose_name='Позиция картинки')
    place = models.ForeignKey(Place,
                              related_name='images',
                              verbose_name='Место',
                              on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', verbose_name="Изображение места")

    class Meta:
        ordering = ['position']
