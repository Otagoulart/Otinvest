"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('duvida/', DuvidaView.as_view(), name='duvida'),
    path('apoio/', ApoioView.as_view(), name='apoio'),
    path('cadastro/', InvestidorView.as_view(), name='investidor'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('forum/', ForumView.as_view(), name='forum'),
    path('investimentos/', TipoInvestView.as_view(), name='tipoinvest'),
    path('investidor/', InvestidorView.as_view(), name='investidor'),
    path('ondeinvestir/', CorretoraView.as_view(), name='corretora'),
    path('perfilinvest/', PerfilInvestView.as_view(), name='perfilinvest'),
    path('topico/<int:topico_id>/', TopicoDetalhesView.as_view(), name='topico_detalhes'),
    path('criar-topico/', CriarTopicoView.as_view(), name='criar_topico'),
    path('forum/editar-topico/<int:topico_id>/', EditarTopicoView.as_view(), name='editar_topico'),
    path('forum/excluir-topico/<int:topico_id>/', ExcluirTopicoView.as_view(), name='excluir_topico'),
    path('comentario/editar/<int:comentario_id>/', Editarcomentario.as_view(), name='editar_comentario'),
]




