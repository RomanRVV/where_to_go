from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import *


def show_main(request):
    features = []
    places = Place.objects.all()
    data = {}
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('places', args=[place.id])
            }
        }
        features.append(feature)
        geojson = {
            "type": "FeatureCollection",
            "features": features
        }
        data = {'geojson': geojson}
    return render(request, 'index.html', context=data)


def show_place(request, place_id):
    requested_place = get_object_or_404(Place, id=place_id)
    place_images = requested_place.images
    place_images_url = [place.image.url for place in place_images.all()]

    response = {
        "title": requested_place.title,
        "imgs": place_images_url,
        "description_short": requested_place.description_short,
        "description_long": requested_place.description_long,
        "coordinates": {
            "lat": requested_place.latitude,
            "lng": requested_place.longitude
        }
    }

    return JsonResponse(response, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 2
                                                     })
