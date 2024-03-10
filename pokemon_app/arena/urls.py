from django.urls import path

from .views import *

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', ArenaView.as_view(), name="arena"),
    path('battle-result/<int:battle_id>/', show_battle_result, name='show_battle_result'),
    path('test', battle_test, name='test'),
]