from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("stream/all", views.all_stream, name="all_stream"),
    path("stream/<slug:slug>", views.stream, name="stream"),
    path("post/<slug:slug>", views.post, name="post"),
]
