from django.urls import path

from apps.adopcion.views import index_adopcion

urlpatterns = [
    path('', index_adopcion),
]