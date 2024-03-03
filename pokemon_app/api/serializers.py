from rest_framework.serializers import ModelSerializer
from pokemon.models import Pokemon


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'