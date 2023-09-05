from django.core.management.base import BaseCommand
import requests
from places.models import *
from django.core.files.base import ContentFile
from urllib.parse import urlparse


class Command(BaseCommand):
    help = 'Загрузка данных на сайт из json файла'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)

    def handle(self, *args, **kwargs):

        def upload_image(place, image_url):
            response = requests.get(image_url)
            response.raise_for_status()
            image_path = urlparse(image_url).path
            image_name = image_path.rstrip('/').split('/')[-1]

            PlacesImage.objects.create(
                place=place,
                image=ContentFile(response.content, name=image_name)
            )

        url = kwargs['json_url']

        response = requests.get(url)
        response.raise_for_status()
        answer = response.json()

        title = answer['title']
        images = answer['imgs']
        description_short = answer['description_short']
        description_long = answer['description_long']
        lng = answer['coordinates']['lng']
        lat = answer['coordinates']['lat']

        place, created = Place.objects.get_or_create(title=title,
                                                     description_short=description_short,
                                                     description_long=description_long,
                                                     longitude=lng,
                                                     latitude=lat)

        for image in images:
            upload_image(place, image)
