# Generated by Django 4.2.3 on 2023-09-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_placesimage_position_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placesimage',
            name='position_1',
        ),
        migrations.AlterField(
            model_name='placesimage',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция картинки'),
        ),
    ]
