# Generated by Django 4.2.3 on 2023-09-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_remove_place_image_placesimage_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placesimage',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Позиция картинки'),
        ),
    ]
