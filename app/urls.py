from django.urls import path
from .views import(
    home,
    desafio
) 

urlpatterns = [
    path("", home, name="home"),
    path("desafio/", desafio, name="desafio"),
]