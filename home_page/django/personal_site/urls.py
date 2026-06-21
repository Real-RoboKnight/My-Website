from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('LICENSE', views.static_page('LICENSE.html'), name='license'),
    path('contact', views.ContactMe.as_view(), name='contact-me'),
    path('test', views.test, name='test'),
]
