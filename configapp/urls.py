from django.urls import path

from configapp.views import *

urlpatterns = [
    path('movie_api/',movie_api),
    path("movie/<slug:slug>/", actor_detail, name="actor-detail"),
    path("actors/", actor_list, name="actor-list"),
    path("actors/<slug:slug>/", actor_detail, name="actor-detail"),
]
