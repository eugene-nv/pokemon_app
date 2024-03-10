import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, DeleteView

from pokemon.forms import PokemonForm
from pokemon.models import Pokemon


from .servises.servises import CreatePokemon


def index(request):
    return render(request, 'pokemon/home.html')


# class PokemonViews(ListView):
#     template_name = 'pokemon/home.html'
#     context_object_name = 'pokemons'


class OwnerPokemonViews(ListView):
    template_name = 'pokemon/user_pokemons.html'
    context_object_name = 'pokemons'

    def get_queryset(self):
        owner_pokemons = len(Pokemon.objects.filter(owner=self.request.user))
        if owner_pokemons == 0:
            first_pokemon = CreatePokemon(self.request.user)
            first_pokemon.create()

        return Pokemon.objects.filter(owner=self.request.user)


def create_pokemon(request):
    if random.choice((True, False)):
        pokemon = CreatePokemon(request.user)
        pokemon.create()

        return redirect('pokemons')
    else:
        return HttpResponse("<h1>Не повезло Попробуй в другой раз</h1>")


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
