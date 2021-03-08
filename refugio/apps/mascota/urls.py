from django.urls import path

from apps.mascota.views import index, mascota_form, mascota_list

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', mascota_form, name='mascota_crear'),
    path('listar', mascota_list, name='mascota_listar'),
]
