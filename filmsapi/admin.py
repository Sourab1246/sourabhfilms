from django.contrib import admin
from .models import Movies,Actors,MoviesActors

# Register your models here.
admin.site.register(Movies),
admin.site.register(Actors),
admin.site.register(MoviesActors),


