import random

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from pokemon.models import Pokemon

from .servises.servises import CreatePokemon


def start(request):
    first_pokemon = CreatePokemon(request.user)
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
        pokemon = CreatePokemon(request.user)
        pokemon.create()
        return redirect('pokemons')
    else:
        return render(request, 'pokemon/did_not_catch.html')


def create_first_pokemon(request):
    pokemon = CreatePokemon(request.user)
    pokemon.create()
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
