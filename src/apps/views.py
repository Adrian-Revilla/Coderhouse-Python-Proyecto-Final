from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
from . import models
from django.forms.models import model_to_dict

from django.urls import resolve

from . import forms, models

from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import F
from django.db import connection


# def dictfetchall(cursor):
# 	"Return all rows from a cursor as a dict"
# 	columns = [col[0] for col in cursor.description]
# 	return [
# 		dict(zip(columns, row))
# 		for row in cursor.fetchall()
# 	]


# def transformar_url(dict):
# 	with connection.cursor() as cursor:
# 		cursor.execute("SELECT c.*, imagen  FROM apps_conductor c");
# 		res = dictfetchall(cursor)

# 	return res

class BaseList(ListView):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#context['object_list'].update(avatar_conductor=F("avatar_conductor") + "aaaaa i am litter butterflai")

		# raise ValueError(transformar_url(dict()), context['object_list'].all().values() )
		return {
			# aqui se me ocurre desempacar a un array de valores. que viene custom.
			'objetos': context['object_list'].all().values(*self.custom_values_list)
		}
	
class BaseDetail(DetailView):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return {
			'datos': model_to_dict(context['object']) 
		}

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def obtener_lista_de_datos(modelo: models):
	return {
		'th': modelo().get_model_fields(),
		'td': list(modelo.objects.values_list()),
		'model_name': modelo()._meta.model_name
	}
	
def nukear_db(request):
	models.Vehiculo.objects.all().delete()
	models.Viaje.objects.all().delete()
	models.Conductor.objects.all().delete()
	return redirect("index")

# --------------------------------------------------------------------

class ConductoresCreate(CreateView):
	model = models.Conductor
	form_class = forms.ConductorForm
	success_url = reverse_lazy("conductores")
	template_name = "conductor_create.html"

class ConductorDetail(BaseDetail):
	model = models.Conductor
	template_name = "conductor_detail.html"

class ConductorList(BaseList):
	model = models.Conductor
	custom_values_list = ['id','avatar_conductor', 'nombre_conductor']
	template_name = "conductor_list.html"

class ConductorUpdate(UpdateView):
	model = models.Conductor
	template_name = "conductor_update.html"
	form_class = forms.ConductorForm
	success_url = reverse_lazy("conductores")

class ConductorDelete(DeleteView):
	model = models.Conductor
	template_name = "conductor_delete.html"
	success_url = reverse_lazy("conductores")

# --------------------------------------------------------------------

class VehiculosCreate(CreateView):
	model = models.Vehiculo
	form_class = forms.VehiculoForm
	success_url = reverse_lazy("vehiculos")
	template_name = "vehiculo_create.html"

class VehiculoDetail(BaseDetail):
	model = models.Vehiculo
	template_name = "vehiculo_detail.html"

class VehiculoList(BaseList):
	model = models.Vehiculo
	template_name = "vehiculo_list.html"
	custom_values_list = ['id', 'nombre_vehiculo']

class VehiculoUpdate(UpdateView):
	model = models.Vehiculo
	template_name = "vehiculo_update.html"
	success_url = reverse_lazy("vehiculos")
	form_class = forms.VehiculoForm
	success_url = reverse_lazy("vehiculos")


class VehiculoDelete(DeleteView):
	model = models.Vehiculo
	template_name = "vehiculo_delete.html"
	success_url = reverse_lazy("vehiculos")

# --------------------------------------------------------------------

class ViajeCreate(CreateView):
	model = models.Viaje
	form_class = forms.ViajeForm
	success_url = reverse_lazy("index")
	template_name = "viaje_create.html"

class ViajeDetail(BaseDetail):
	model = models.Viaje
	template_name = "viaje_detail.html"

class ViajeList(BaseList):
	model = models.Viaje
	template_name = "viaje_list.html"
	custom_values_list = ['id','avatar_cliente', 'nombre_del_pasajero']
	
	
class ViajeUpdate(UpdateView):
	model = models.Viaje
	template_name = "viaje_update.html"
	form_class = forms.ViajeForm
	success_url = reverse_lazy("index")

class ViajeDelete(DeleteView):
	model = models.Viaje
	template_name = "viaje_delete.html"
	success_url = reverse_lazy("index")



# ------------------------------------------------------------------

class RegisterView(SuccessMessageMixin, CreateView):
  template_name = 'register.html'
  success_url = reverse_lazy('index')
  form_class = forms.UserCreate
  success_message = "Your profile was created successfully"