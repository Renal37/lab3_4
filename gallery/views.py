import requests
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def gallery_view(request: HttpRequest) -> HttpResponse:

    url = "https://dog.ceo/api/breeds/image/random/10"
    response = requests.get(url)
    data = response.json()
    images = data['message']

    return render(request, 'gallery/index.html', {'images': images})
