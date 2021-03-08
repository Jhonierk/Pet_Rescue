from django.urls import path

from apps.mascota.views import index, mascota_form

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', mascota_form, name='mascota_crear'),
]
