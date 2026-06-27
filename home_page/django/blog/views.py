from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "This is a test page. It is not meant to be used in production."
    )
