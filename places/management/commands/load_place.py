from urllib.parse import urlparse

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests

from places.models import Place, PlacesImage


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
        payload = response.json()

        title = payload['title']
        images = payload['imgs']
        short_description = payload.get('short_description', '')
        long_description = payload.get('long_description', '')
        lng = payload['coordinates']['lng']
        lat = payload['coordinates']['lat']

        place, created = Place.objects.get_or_create(title=title,
                                                     longitude=lng,
                                                     latitude=lat,
                                                     defaults={
                                                         'short_description': short_description,
                                                         'long_description': long_description,
                                                     })

        for image in images:
            upload_image(place, image)
