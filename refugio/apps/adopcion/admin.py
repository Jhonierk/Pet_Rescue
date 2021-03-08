from django.contrib import admin

#impotar el modelo de la app:

from apps.adopcion.models import Persona

# Register your models here.
admin.site.register(Persona)