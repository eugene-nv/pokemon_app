import random

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from arena.models import Arena
from arena.servises.system import ArenaSystem
from pokemon.models import Pokemon
from users.models import User


from .servises.system import PokemonSystem


def start(request):
    first_pokemon = PokemonSystem()
    first_pokemon.create_pokemon(request.user)
    return render(request, 'pokemon/start.html', {'first_pokemon': first_pokemon})


def home(request):
    if request.user.is_authenticated:
        return redirect('pokemons')
    else:
        return render(request, 'pokemon/home.html')


class OwnerPokemonViews(ListView):
    template_name = 'pokemon/user_pokemons.html'
    context_object_name = 'pokemons'

    def get_queryset(self):
        return Pokemon.objects.filter(owner=self.request.user)


def create_pokemon(request):
    if random.choice((True, False)):
        pokemon = PokemonSystem()
        pokemon.create_pokemon(request.user)
        return redirect('pokemons')
    else:
        return render(request, 'pokemon/did_not_catch.html')


def create_first_pokemon(request):
    pokemon = PokemonSystem()
    pokemon.create_pokemon(request.user)
    return redirect('pokemons')


class ShowPokemon(DetailView):
    model = Pokemon
    template_name = 'pokemon/pokemon_card.html'
    context_object_name = 'pokemon'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class PokemonDeleteView(DeleteView):
    model = Pokemon
    success_url = reverse_lazy("pokemons")
    context_object_name = 'pokemon'
    template_name = 'pokemon/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


def test(request):
    x = ArenaSystem()
    x.start()
    context = {

    }
    return render(request, 'test.html', context)
