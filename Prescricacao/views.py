from django.views.generic import View,CreateView,FormView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *


# Create your views here.

class Autenticacao(View):

    def get(self, request):
        context = {}

        if self.request.user and self.request.user.is_active:
            return render(request, 'index.html', context)
        return render(request, 'autenticacao/login.html', context)

    def post (self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password = password)
        context = {}
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect ('/')
            else:
                context.update(mensagem = 'Usuario Inativo')
        else:                                  
            context.update(mensagem='Usuario ou senha Incorreta')
        return render(request, 'autenticacao/login.html', context)

def sair(request):
    print ("logout")
    logout(request)
    return redirect ('/')

class CriarTarefas(CreateView):
    model= PrescricaoDeEnfermagem
    form_class= Formularios
    template_name= 'tarefas/criar.html'
    success_url='/'
