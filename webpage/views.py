from django.shortcuts import render
from webpage.models import *

def index(request):
	return render(request, "index.html")

def mapa(request):
	return render(request, "mapa.html")