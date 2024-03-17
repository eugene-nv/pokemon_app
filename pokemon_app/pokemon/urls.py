from django.urls import path

from .views import *

urlpatterns = [
    path('start/', start, name='start'),
    path('', home, name='home'),
    path('pokemon/', OwnerPokemonViews.as_view(), name='pokemons'),
    path('pokemon/<int:pk>/', ShowPokemon.as_view(), name='show_pokemon'),
    path('pokemon/<int:pk>/delete/', PokemonDeleteView.as_view(), name='delete_pokemon'),
    path('create/', create_pokemon, name='create'),
    path('create_first_pokemon/', create_first_pokemon, name='create_first_pokemon'),


]