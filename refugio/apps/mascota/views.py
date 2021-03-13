from django.shortcuts import render, redirect
from django.http import HttpResponse
#importacion usando ListView y CreateView de la clase mascota:
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#se importa el reverse_lazy
from django.urls import reverse_lazy

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
# Create your views here.


#Vistas basadas en funcion:

def index(request):
	return render(request, "mascota/index.html")

def mascota_form(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota_listar')
	else:
		form = MascotaForm()
	return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id') #ordenar por id
	contexto = {'mascotas': mascota}
	return render(request,'mascota/mascota_list.html', contexto)

#actualizacion
def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota_listar')
	return render(request, 'mascota/mascota_form.html', {'form':form})

#funcion que elimina un objeto del modelo mascota
def mascota_delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota_listar')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})

#aqui no se define una funcion, se declara una clase
#Vistas basadas en clases:
#esta clase lista todos los objetos del modelo mascota
class MascotaList(ListView):
	#indicar el modelo
	model = Mascota
	#a que template enviar
	template_name = 'mascota_list'
#hereda de la clase generica ListView (necesita ser importada)
#Mas informacion en la documentacion : https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#listview

#ahora un CreateView
#Tambien se importa

class MascotaCreate(CreateView):
	#idicar modelo
	model = Mascota
	#que formulacio utilizar para crear
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	#Como redirigir una url cuando guardamos nuestros registros:
	#con el atibuto  success_url se usa el revere_lazy 
	success_url = reverse_lazy('mascota_listar')


class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota_listar')

class MascotaDelete(DeleteView):
	model = Mascota
	template_name = 'mascota/mascota_delete.html'
	success_url = reverse_lazy('mascota:mascota_listar')
