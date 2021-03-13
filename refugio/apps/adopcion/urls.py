from django.urls import path

from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate

urlpatterns = [
    path('', index_adopcion),
    path('solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
]