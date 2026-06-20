from typing import Callable

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .forms import Contact_Me
# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'framework/main.html', {'title': 'Home', 'body': 'This is the home page of my personal website. Welcome!'})


def static_page(template_path: str) -> Callable[[HttpRequest], HttpResponse]:
    def view(request: HttpRequest) -> HttpResponse:
        return render(request, template_path)
    return view


class ContactMe(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        print("Form gotten valid.")

        return render(request, 'Contact.html', {'form': Contact_Me})

    def post(self, request: HttpRequest) -> HttpResponse:
        print("Processing the form...")
        form = Contact_Me(request.POST)
        if form.is_valid():
            # Process the form data here (e.g., send an email)
            return HttpResponse('Valid Data')

        return render(request, 'Contact.html', {'form': Contact_Me(request.POST)})
