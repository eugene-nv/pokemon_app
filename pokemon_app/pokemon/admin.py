from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Pokemon


@admin.register(Pokemon)
class CharacterAdmin(ModelAdmin):
    pass