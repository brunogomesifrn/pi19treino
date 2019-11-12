from django.shortcuts import render, redirect
from .form import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, "index.html")

@login_required
def treinos(request):
	return render(request, "treinos.html")

def registro(request):

	form = UserForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
		'form': form
	}
	return render(request, 'registration/register.html', contexto)

def do_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user == None:
			return HttpResponse("<h1 align='center'># Senha errada ou usuário</h1>")
		else:
			if user.is_active:
				login(request, user)
				return redirect('index')
	else:
		return render(request, 'registration/login.html')


