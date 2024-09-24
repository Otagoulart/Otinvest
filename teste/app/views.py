
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
        apoio = apoio.objects.all()
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




from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Topico, Comentario

class ForumView(View):
    def get(self, request):
        topicos = Topico.objects.all().order_by('-criado_em')
        return render(request, 'forum.html', {'topicos': topicos})

class TopicoDetalhesView(View):
    def get(self, request, topico_id):
        topico = get_object_or_404(Topico, id=topico_id)
        comentarios = topico.comentarios.all()
        return render(request, 'topico_detalhes.html', {'topico': topico, 'comentarios': comentarios})

    def post(self, request, topico_id):
        topico = get_object_or_404(Topico, id=topico_id)
        conteudo = request.POST.get('conteudo')
        Comentario.objects.create(
            topico=topico, conteudo=conteudo, autor=request.user
        )
        messages.success(request, 'Comentário adicionado com sucesso!')
        return redirect('topico_detalhes', topico_id=topico.id)

class CriarTopicoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'criar_topico.html')

    def post(self, request):
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        Topico.objects.create(
            titulo=titulo, conteudo=conteudo, autor=request.user
        )
        messages.success(request, 'Tópico criado com sucesso!')
        return redirect('forum')
class EditarTopicoView(View):
    def get(self, request, topico_id):
        topico = get_object_or_404(Topico, id=topico_id)
        return render(request, 'editar_topico.html', {'topico': topico})

    def post(self, request, topico_id):
        topico = get_object_or_404(Topico, id=topico_id)
        topico.titulo = request.POST.get('titulo')
        topico.save()
        return redirect('forum')  # Redireciona de volta para o fórum
       
class ExcluirTopicoView(View):
    def post(self, request, topico_id):
        topico = get_object_or_404(Topico, id=topico_id)
        topico.delete()
        return redirect('forum')
    
class Editarcomentario(View):
    def editar_comentario(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)

        if request.method == "POST":
            comentario.conteudo = request.POST.get("conteudo")
            comentario.save()
            return redirect('topico_detalhes', topico_id=comentario.topico.id)  # Redireciona para a página do tópico

        return render(request, 'editar_comentario.html', {'comentario': comentario})