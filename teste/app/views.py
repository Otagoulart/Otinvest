
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