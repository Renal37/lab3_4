
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about/about.html')


