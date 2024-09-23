
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class DuvidaView(View):
    def get(self, request,):
        duvida = Duvida.objects.all()
        return render(request, 'duvida.html', {'duvidas':duvida})
    def post(self, request):
        pass

class ApoioView(View):
    def get(self, request,):
        apoio = Apoio.objects.all()
        return render(request, 'apoio.html', {'apoios':apoio})
    def post(self, request):
        pass

class InvestidorView(View):
    def get(self, request,):
        investidor = Investidor.objects.all()
        return render(request, 'cadastro.html', {'investidores':investidor})
    def post(self, request):
        pass

class PerfilInvestView(View):
    def get(self, request,):
        perfilinvest = PerfilInvest.objects.all()
        return render(request, 'perfilinvest.html', {'perfilinvest':perfilinvest})
    def post(self, request):
        pass

class ContatoView(View):
    def get(self, request,):
        contato = Contato.objects.all()
        return render(request, 'contato.html', {'contatos':contato})
    def post(self, request):
        pass


class  SegurancaView(View):
    def get(self, request,):
        seguranca= Seguranca.objects.all()
        return render(request, 'forum.html', {'seguranca':seguranca})
    def post(self, request):
        pass

class CorretoraView(View):

    def get(self, request,):
        corretora = Corretora.objects.all()
        return render(request, 'ondeinvestir.html', {'corretoras':corretora})
    def post(self, request):
        pass


class TipoInvestView(View):
    def get(self, request,):
        tipoinvest = TipoInvest.objects.all()
        return render(request, 'investimento.html', {'tipoinvest':tipoinvest})
    def post(self, request):
        pass

class LoginView(View):
    def get(self, request,):
        login = Login.objects.all()
        return render(request, 'login.html', {'logins':login})
    def post(self, request):
        pass

