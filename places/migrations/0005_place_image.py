# Generated by Django 4.2.3 on 2023-09-03 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_placesimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.placesimage', verbose_name='Картинки'),
        ),
    ]
