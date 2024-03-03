from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from pokemon.models import Pokemon
from .serializers import PokemonSerializer


class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()