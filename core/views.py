from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "index.html")

def treinos(request):
	return render(request, "treinos.html")