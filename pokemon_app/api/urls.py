from rest_framework.routers import SimpleRouter

from .views import PokemonViewSet

router = SimpleRouter()

router.register(r'pokemon', PokemonViewSet)

urlpatterns = []

urlpatterns += router.urls