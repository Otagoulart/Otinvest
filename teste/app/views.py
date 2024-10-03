from django.shortcuts import render, redirect, get_object_or_404
from .models import *  # Certifique-se de que você só importa o que precisa
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Topico, Comentario, Duvida, Apoio, Investidor, PerfilInvest, Corretora, TipoInvest, Seguranca  # Adicione os modelos que você utiliza
from .forms import InvestidorForm
# View para a página inicial
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

# View para dúvidas
class DuvidaView(View):
    def get(self, request):
        duvidas = Duvida.objects.all()
        return render(request, 'duvida.html', {'duvidas': duvidas})

# View para apoio
class ApoioView(View):
    def get(self, request):
        apoio_list = Apoio.objects.all()  # Certifique-se de que o modelo é definido corretamente
        return render(request, 'apoio.html', {'apoios': apoio_list})

# View para cadastro de investidores
class InvestidorView(View):
    def get(self, request):
        form = InvestidorForm()  # Cria uma instância vazia do formulário
        return render(request, 'cadastro.html', {'form': form})

    def post(self, request):
        form = InvestidorForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o formulário se for válido
            return redirect('sucesso')  # Redireciona para a URL de sucesso
        return render(request, 'cadastro.html', {'form': form})  # Retorna o formulário com erros se inválido

class PerfilInvestView(View):
    def get(self, request):
        perfis_invest = PerfilInvest.objects.all()
        return render(request, 'perfilinvest.html', {'perfilinvest': perfis_invest})


# View para contato
class ContatoView(View):
    def get(self, request):
        contatos = Contato.objects.all()
        return render(request, 'contato.html', {'contatos': contatos})

# View para segurança
class SegurancaView(View):
    def get(self, request):
        seguranca = Seguranca.objects.all()
        return render(request, 'forum.html', {'seguranca': seguranca})

# View para corretoras
class CorretoraView(View):
    def get(self, request):
        corretoras = Corretora.objects.all()
        return render(request, 'ondeinvestir.html', {'corretoras': corretoras})

# View para tipos de investimento
class TipoInvestView(View):
    def get(self, request):
        tipos_invest = TipoInvest.objects.all()
        return render(request, 'investimento.html', {'tipoinvest': tipos_invest})

# View para o fórum
class ForumView(View):
    def get(self, request):
        topicos = Topico.objects.all().order_by('-criado_em')
        return render(request, 'forum.html', {'topicos': topicos})

# View para detalhes do tópico
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

# View para criar tópico
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

# View para editar tópico
class EditarTopicoView(View):
    def get(self, request, topico_id):
        topico = get_object_or_404(Topico, id=topico_id)
        return render(request, 'editar_topico.html', {'topico': topico})

    def post(self, request, topico_id):
        topico = get_object_or_404(Topico, id=topico_id)
        topico.titulo = request.POST.get('titulo')
        topico.conteudo = request.POST.get('conteudo')  # Não se esqueça de atualizar o conteúdo
        topico.save()
        return redirect('forum')  # Redireciona de volta para o fórum

# View para excluir tópico
class ExcluirTopicoView(View):
    def post(self, request, topico_id):
        topico = get_object_or_404(Topico, id=topico_id)
        topico.delete()
        messages.success(request, 'Tópico excluído com sucesso!')
        return redirect('forum')

class EditarComentarioView(View):  # Use a convenção de nomenclatura correta
    def get(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        return render(request, 'editar_comentario.html', {'comentario': comentario})

    def post(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        novo_conteudo = request.POST['conteudo']
        comentario.conteudo = novo_conteudo
        comentario.save()
        return redirect('detalhes_topico')  # Ajuste conforme necessário

# View para a página de sucesso
class SucessoView(View):
    template_name = 'cadastro/sucesso.html'  # Caminho do template

    def get(self, request):
        return render(request, self.template_name)
