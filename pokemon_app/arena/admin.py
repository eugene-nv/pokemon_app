from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Arena, Log


@admin.register(Arena)
class ArenaAdmin(ModelAdmin):
    pass


@admin.register(Log)
class LogAdmin(ModelAdmin):
    pass