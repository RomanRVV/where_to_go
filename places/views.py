from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def show_main(request):
    features = []
    places = Place.objects.all()
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
    context = {'geojson': geojson}
    return render(request, 'index.html', context=context)


def show_place(request, place_id):
    requested_place = get_object_or_404(Place, id=place_id).prefetch_related('images')
    place_images = requested_place.images
    place_images_url = [place.image.url for place in place_images.all()]

    response = {
        "title": requested_place.title,
        "imgs": place_images_url,
        "description_short": requested_place.short_description,
        "description_long": requested_place.long_description,
        "coordinates": {
            "lat": requested_place.latitude,
            "lng": requested_place.longitude
        }
    }

    return JsonResponse(response, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 2
                                                     })
