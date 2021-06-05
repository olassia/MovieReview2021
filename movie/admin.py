from django.contrib import admin
from .models import MovieType, Film, Review
# Register your models here.

admin.site.register(MovieType)
admin.site.register(Film)
admin.site.register(Review)
