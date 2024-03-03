from django.shortcuts import render
from django.views.generic import ListView
from pokemon.models import Pokemon
from .models import Arena
from .servises.battle import CreateBattle, Battle


def battle_main(request):
    create = Battle(request.user)
    create.battle()

    return render(request, 'battle/battle.html', {'create': create})