from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pokemon_app import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('pokemon.urls')),

    path('arena/', include('arena.urls')),

    path('api/', include('api.urls')),

    path('users/', include('users.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
