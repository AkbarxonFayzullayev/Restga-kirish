from django.contrib import admin

from configapp.models import Actors, Movie

# Register your models here.
admin.site.register([Actors,Movie])