import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, DeleteView

from pokemon.forms import PokemonForm
from pokemon.models import Pokemon

from .servises.instance_data_generator import Generator


def index(request):
    return render(request, 'pokemon/home.html')


# class PokemonViews(ListView):
#     template_name = 'pokemon/home.html'
#     context_object_name = 'pokemons'


class OwnerPokemonViews(ListView):
    template_name = 'pokemon/user_pokemons.html'
    context_object_name = 'pokemons'

    def get_queryset(self):
        return Pokemon.objects.filter(owner=self.request.user)


class CreatePokemon(CreateView):
    form_class = PokemonForm
    template_name = 'pokemon/create.html'
    success_url = reverse_lazy('pokemons')

    model = Pokemon

    def form_valid(self, form):
        if random.choice((True, False)):

            p = Generator()

            instance = form.save(commit=False)
            instance.owner = self.request.user
            instance.name = p.name
            instance.portrait = p.portrait
            instance.experience = 0
            instance.level = 1
            instance.hp = p.hp
            instance.strength = p.strength
            instance.constitution = p.constitution
            instance.win_count = 0
            instance.defeat_count = 0
            instance.save()

            return super().form_valid(form)
        else:
            return HttpResponse("<h1>Не повезло</h1>")


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