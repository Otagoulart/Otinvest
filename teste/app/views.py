
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
    
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comentario

class Editarcomentario(View): 
    def editar_comentario(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)

        if request.method == 'POST':
            # Atualiza o conteúdo do comentário com os novos dados
            novo_conteudo = request.POST['conteudo']
            comentario.conteudo = novo_conteudo
            comentario.save()
            # Redireciona de volta para a página do tópico ou onde os comentários estão listados
            return redirect('detalhes_topico')  # Alterar se for diferente o nome da página principal

        return render(request, 'editar_comentario.html', {'comentario': comentario})

from django.shortcuts import render, redirect
from .models import Investidor  # Supondo que você tenha um modelo chamado Investidor
from .forms import InvestidorForm  # Supondo que você tenha um formulário para o Investidor

class InvestidorView(View):
    def get(self, request):
        form = InvestidorForm()  # Cria uma instância vazia do formulário
        return render(request, 'cadastro.html', {'form': form})  # Retorna a página com o formulário

    def post(self, request):
        form = InvestidorForm(request.POST)
        if form.is_valid():
            investidor = form.save()  # Salva o formulário se for válido
            return redirect('sucesso.html')  # Redireciona para uma URL de sucesso
        return render(request, 'cadastro.html', {'form': form})  # Retorna o formulário com erros se inválido

from django.views.generic import TemplateView

class SucessoView(View):
    template_name = 'cadastro/sucesso.html'; # Caminho do template
