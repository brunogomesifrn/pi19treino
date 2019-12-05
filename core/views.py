from django.shortcuts import render, redirect
from .form import UserForm, TreinoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Regiao_corporal, Tempo_repeticao, Intervalo_treinos, Treino

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


@login_required
def editar(request, id):
	user = User.objects.get(pk=id)
	form = UserForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
		'form': form
	}
	return render(request, 'registration/register.html', contexto)

@login_required
def meustreinos(request):
	data = {}
	treinos = Treino.objects.filter(user=request.user)
	data['treinos'] = treinos

	return render(request, 'meustreinos.html', data)



@login_required
def cadastrartreinos(request):
	data = {}
	if request.method == 'POST':
		form = TreinoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			return HttpResponse('Erro')
	else:
		form = TreinoForm(initial={'user':request.user})

	data['form'] = form
	return render(request, 'cadastrar-treinos.html', data)




