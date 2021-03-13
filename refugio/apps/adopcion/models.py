from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length = 70)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)

class Solicitud(models.Model):
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()

#cada vez que se crea un nuevo modelo se tiene que dar makemigratios para que realize los cambiar y migrate para subirlo a la base de datos