from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		#Aqui se colocan los campos del modelo
		fields = [
			'animal',
			'raza',
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
		]

		#Diccionario:

		labels = {
			'animal': 'Animal',
			'raza': 'Raza',
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad_aproximada',
			'persona': 'Adoptante',
			'vacuna': 'Vacuna',
		}

		widgets = {
			'animal': forms.TextInput(attrs={'class':'form-control'}),
			'raza': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),
		}