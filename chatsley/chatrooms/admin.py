from django.contrib import admin

# Register your models here.
from .models import Room

admin.site.register(Room)

# Displays room models inside the admin url
