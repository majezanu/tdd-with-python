from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="home.html")
