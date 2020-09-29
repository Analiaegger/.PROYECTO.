from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CreateUserForm, ProductCreationForm
import os,sys
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario
from apps.productos.models import Producto
from django.urls import reverse_lazy

from django.template import Template,Context
from django.http import HttpResponse


class signIn(CreateView):
    model = Usuario
    form_class = CreateUserForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')

class CreateProduct(CreateView):
	model = Producto
	form_class = ProductCreationForm
	template_name = 'productos/crear.html'
	success_url = reverse_lazy('login')

def pagEmprendedor(request):
	doc_ext = open("D:/INFO2020/RepositorioInfo/PROYECTO/infoProject/infoProject/templates/emprendedores/vistaEmprendedor.html")
	plt = Template(doc_ext.read())
	doc_ext.close()
	ctx = Context()
	doc = plt.render(ctx)
	return HttpResponse(doc)

def Inicio(request):
	doc_ext = open("D:/INFO2020/RepositorioInfo/PROYECTO/infoProject/infoProject/templates/inicio.html")
	plt = Template(doc_ext.read())
	doc_ext.close()
	ctx = Context()
	doc = plt.render(ctx)
	return HttpResponse(doc)

def About(request):
	doc_ext = open("D:/INFO2020/RepositorioInfo/PROYECTO/infoProject/infoProject/templates/about.html")
	plt = Template(doc_ext.read())
	doc_ext.close()
	ctx = Context()
	doc = plt.render(ctx)
	return HttpResponse(doc)
