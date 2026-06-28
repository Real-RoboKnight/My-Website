from typing import Callable

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import View
from django.core.mail import send_mail, EmailMultiAlternatives

from .forms import Contact_Me
# Create your views here.


def static_page(template_path: str) -> Callable[[HttpRequest], HttpResponse]:
    def view(request: HttpRequest) -> HttpResponse:
        return render(request, template_path)

    return view


class ContactMe(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        print("Form gotten valid.")

        return render(request, "Contact.html", {"form": Contact_Me()})

    def post(self, request: HttpRequest) -> HttpResponse:
        print("Processing the form...")
        form = Contact_Me(request.POST)
        if not form.is_valid():
            return render(request, "Contact.html", {"form": form}, status=400)

        email = EmailMultiAlternatives(
            subject=f"[Website Contact Request] {request.POST.get('subject')}",
            to=["website.contact@dylan-shah.com"],
            from_email=f"{request.POST.get('name')} | Website Contact Request <contact-request.website@dylan-shah.com>",
            reply_to=[request.POST.get("response_email")],  # pyright: ignore[reportArgumentType]
            body="",
        )
        email.attach_alternative(
            render_to_string(
                "email_contact.html",
                {
                    "name": request.POST.get("name"),
                    "email": request.POST.get("response_email"),
                    "subject": request.POST.get("subject"),
                    "message": request.POST.get("content"),
                },
            ),
            "text/html",
        )
        email.send(fail_silently=True)
        return render(
            request,
            "email_contact.html",
            {
                "name": request.POST.get("name"),
                "email": request.POST.get("response_email"),
                "subject": request.POST.get("subject"),
                "message": request.POST.get("content"),
            },
        )


def test(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "This is a test page. It is not meant to be used in production."
    )
