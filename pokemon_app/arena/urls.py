from django.urls import path

from .views import *

urlpatterns = [
    path('', battle_main, name='arena'),



]