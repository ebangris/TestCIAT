from django.db import models

class Mapa():
	latitud = models.IntegerField()
	longitud = models.IntegerField()

class Animales(models.Model, Mapa):
	propietario = models.CharField(max_length=80)
	cantidad = models.IntegerField(null=True)
	informacion = models.TextField(null=True)

	def __str__(self):
		return self.propietario

class Deforestacion(models.Model, Mapa):
	number = models.IntegerField(primary_key=True)
	area = models.IntegerField()
	cambio = models.IntegerField()
	
	def __str__(self):
		return self.pk
	