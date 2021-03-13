from django.urls import path


from apps.mascota.views import index, mascota_form, mascota_list, mascota_edit, mascota_delete

#importacion vistas basadas en clases
from apps.mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', MascotaCreate.as_view(), name='mascota_crear'),
    #path('listar', mascota_list, name='mascota_listar'),
    #Ahora se le agrega la vista basada en clases:
    #como MascotaList es una clase se usa el metodo: .as_view para que lo ejecute como una vista
    path('listar', MascotaList.as_view(), name='mascota_listar'),
    path('editar/<pk>/', MascotaUpdate.as_view(), name='mascota_editar'),
    path('eliminar/<pk>/', MascotaDelete.as_view(), name='mascota_eliminar')


]
