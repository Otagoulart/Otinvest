from django.contrib import admin
from .models import Duvida, Investidor, PerfilInvest, Seguranca, Contato, TipoInvest, Corretora

class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 1  # Número de formulários em branco a serem exibidos

class TipoInvestInline(admin.TabularInline):
    model = TipoInvest
    extra = 1

class CorretoraInline(admin.TabularInline):
    model = Corretora
    extra = 1

class InvestidorAdmin(admin.ModelAdmin):
    list_display = ["id_investidor", "nome", "cpf", "datanasc", "endereco", "cidade", "email"]
    search_fields = ["nome", "cpf", "email"]
    inlines = [ContatoInline, TipoInvestInline, CorretoraInline]



class DuvidaAdmin(admin.ModelAdmin):
    list_display = ["id", "duvida"]  # Aqui 'id' refere-se ao campo padrão
    search_fields = ["duvida"]


class PerfilInvestAdmin(admin.ModelAdmin):
    list_display = ["id_capitalinvest", "descricao", "salario", "investidor"]
    search_fields = ["descricao", "investidor__nome"]

class SegurancaAdmin(admin.ModelAdmin):
    list_display = ["id", "titulo", "investidor"]
    search_fields = ["titulo", "investidor__nome"]

class ContatoAdmin(admin.ModelAdmin):
    list_display = ["id", "numero", "email", "investidor"]
    search_fields = ["email", "numero", "investidor__nome"]


class TipoInvestAdmin(admin.ModelAdmin):
    list_display = ["id", "tipo_de_investimento", "area", "investidor"]
    search_fields = ["tipo_de_investimento", "area", "investidor__nome"]

class CorretoraAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "area", "avaliacao", "investidor"]
    search_fields = ["nome", "area", "investidor__nome"]

