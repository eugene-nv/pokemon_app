from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('', index),
    path('pokemon/', OwnerPokemonViews.as_view(), name='pokemons'),
    path('pokemon/<int:pk>/', ShowPokemon.as_view(), name='show_pokemon'),
    path('pokemon/<int:pk>/delete/', PokemonDeleteView.as_view(), name='delete_pokemon'),
    # path('pokemon/<int:pk>/update/', CharacterUpdateView.as_view(), name='update_character'),
    path('create/', CreatePokemon.as_view(), name='create'),


]