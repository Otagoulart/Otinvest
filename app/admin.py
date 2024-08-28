from django.contrib import admin
from .models import Duvida, Investidor, PerfilInvest, Seguranca, Contato, TipoInvest, Corretora

class ContatoInline(admin.TabularInline):
    model = Contato

class TipoInvestInline(admin.TabularInline):
    model = TipoInvest

class CorretoraInline(admin.TabularInline):
    model = Corretora

@admin.register(Investidor)
class InvestidorAdmin(admin.ModelAdmin):
    list_display = ["id_investidor", "nome", "cpf", "datanasc", "endereco", "cidade", "email"]
    search_fields = ["nome", "cpf", "email"]
    inlines = [ContatoInline, TipoInvestInline, CorretoraInline]

@admin.register(Duvida)
class DuvidaAdmin(admin.ModelAdmin):
    list_display = ["id", "duvida"]
    search_fields = ["duvida"]

@admin.register(PerfilInvest)
class PerfilInvestAdmin(admin.ModelAdmin):
    list_display = ["id_capitalinvest", "descricao", "salario", "investidor"]
    search_fields = ["descricao", "investidor__nome"]

@admin.register(Seguranca)
class SegurancaAdmin(admin.ModelAdmin):
    list_display = ["id", "titulo", "investidor"]
    search_fields = ["titulo", "investidor__nome"]

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ["id", "numero", "email", "investidor"]
    search_fields = ["email", "numero", "investidor__nome"]

@admin.register(TipoInvest)
class TipoInvestAdmin(admin.ModelAdmin):
    list_display = ["id", "tipo_de_investimento", "area", "investidor"]
    search_fields = ["tipo_de_investimento", "area", "investidor__nome"]

@admin.register(Corretora)
class CorretoraAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "area", "avaliacao", "investidor"]
    search_fields = ["nome", "area", "investidor__nome"]
