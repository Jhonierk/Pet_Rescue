from django.urls import path

from apps.mascota.views import index_mascota

urlpatterns = [
    path('', index_mascota),
]
