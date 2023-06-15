from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class Vehiculo(models.Model):
	nombre_vehiculo = models.CharField(max_length=100, blank=False, null=False, unique=True)
	fecha_de_fabricacion = models.DateField(blank=False, null=False)
	patente = models.TextField(blank=False, null=False)
	

	def get_detail_page(self):
		return f"{self._meta.model_name}/{self.id}"


	def get_model_fields(self):
		return [field.name.replace('_', ' ') for field in self._meta.get_fields()]


	def __str__(self):
		return f"{self.nombre_vehiculo} - {self.fecha_de_fabricacion} - {self.patente} "


class Conductor(models.Model):
	nombre_conductor = models.CharField(max_length=100, null=False, unique=True)
	edad = models.PositiveSmallIntegerField(null=False)
	avatar_conductor = models.ImageField(upload_to="avatars", blank=True, null=True)
	fecha_ingreso = models.DateTimeField(blank=False, null=False)

	def get_detail_page(self):
		return f"{self._meta.model_name}/{self.id}"

	def get_model_fields(self):
		return [field.name.replace('_', ' ') for field in self._meta.get_fields()]


	def __str__(self):
		return f"{self.nombre_conductor} - {self.edad}"



class Viaje(models.Model):
	avatar_cliente = models.ImageField(upload_to="avatars", blank=True, null=True)
	nombre_del_pasajero = models.CharField(max_length=100, blank=False, null=False, unique=True)
	inicio_viaje = models.DateTimeField(blank=False, null=False)
	fin_viaje = models.DateTimeField(blank=False, null=False)
	medidor_cliente_satisfecho = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

	def get_detail_page(self):
		return f"{self._meta.model_name}/{self.id}"

	def get_model_fields(self):
		return [field.name.replace('_', ' ') for field in self._meta.get_fields()]


	def __str__(self):
		return f"{self.nombre_del_pasajero} - [INICIO VIAJE: {self.inicio_viaje} - FINAL_VIAJE: {self.fin_viaje}]"