from django.urls import path

from apps.mascota.views import index_mascota, mascota_form

urlpatterns = [
    path('', index_mascota, name='index'),
    path('nuevo', mascota_form, name='mascota_crear'),
]
