from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def show_main(request):
    places = Place.objects.all()
    features = [{
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
        for place in places

    ]
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    context = {'geojson': geojson}
    return render(request, 'index.html', context=context)


def show_place(request, place_id):
    requested_place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)
    place_images_url = [image.image.url for image in requested_place.images.all()]

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
