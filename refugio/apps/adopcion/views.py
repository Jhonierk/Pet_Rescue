from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.adopcion.models import Persona, Solicitud

from apps.adopcion.forms import PersonaForm, SolicitudForm

def index_adopcion(request):
	return HttpResponse("adopcion")

class SolicitudList(ListView):
	model = Solicitud
	template_name = 'adopcion/solicitud_list.html'
	
class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	#Para agregar un segundo formulario:
	second_form_class = PersonaForm
	success_url = reverse_lazy('solicitud_listar')

	#sobre esritura: y agregar los formularios en el contexto
	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	#Sobre escribir el metodo POST
	def post(self, request, *args, **kwargs):
		#Acceder al objeto:
		self.object = self.get_object
		#recoger la informacion de los context y se recogen el POST del primer y segund formulario
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		# Con esto se comprueba si los valores son validos Para guardar:
		if form.is_valid() and form2.is_valid():#Valida la informacion
			#con commit=False impide que los valores se guarden hasta que se guarde el segundo formulacio
			solicitud = form.save(commit=False)#guarda el primer form y se lo asigna a soliciud
			solicitud.persona = form2.save() #Crea la relacion y guarda los valores del segundo form
			solicitud.save()#Guarda el objeto 
			#Se importa
			return HttpResponseRedirect(self.get_success_url())
		else:#si no es valido se devuelve el contexto
			return self.render_to_response(self.get_context_data(form=form, form2=form2))