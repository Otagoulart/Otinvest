from django.db import models

class Duvida(models.Model):
    duvida = models.TextField()

    class Meta:
        verbose_name_plural = "Dúvidas"

    def __str__(self):
        return self.duvida

class Investidor(models.Model):
    id_investidor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    datanasc = models.DateField()
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Investidores"

    def __str__(self):
        return f"{self.nome} - {self.id_investidor}"

from django.db import models

class PerfilInvest(models.Model):
    id_capitalinvest = models.DecimalField(
    max_digits=10, 
    decimal_places=2, 
    primary_key=True, 
    default=100  
)
    investidor = models.ForeignKey('Investidor', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Perfis de Investimento"

    def __str__(self):
        return self.descricao


class Seguranca(models.Model):
    titulo = models.CharField(max_length=50)
    dicas = models.TextField()
    investidor = models.ForeignKey(Investidor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Seguranças"

    def __str__(self):
        return self.titulo

class Contato(models.Model):
    numero = models.CharField(max_length=15)
    email = models.EmailField()
    relato_feedback = models.TextField()
    investidor = models.ForeignKey(Investidor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Contatos"

    def __str__(self):
        return self.email

class TipoInvest(models.Model):
    tipo_de_investimento = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    relato = models.TextField()
    dicas = models.TextField()
    investidor = models.ForeignKey(Investidor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Tipos de Investimentos"

    def __str__(self):
        return self.tipo_de_investimento

class Corretora(models.Model):
    nome = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    avaliacao = models.FloatField()
    investidor = models.ForeignKey(Investidor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Corretoras"

    def __str__(self):
        return self.nome

from django.db import models
from django.contrib.auth.models import User

class Topico(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    topico = models.ForeignKey(Topico, related_name='comentarios', on_delete=models.CASCADE)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} em {self.topico}"

