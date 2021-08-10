from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>", views.showpost, name='showpost'),
    path("", views.homepage, name='index')
]