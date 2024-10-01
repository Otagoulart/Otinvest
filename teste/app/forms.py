from django import forms
from .models import Investidor

class InvestidorForm(forms.ModelForm):
    class Meta:
        model = Investidor
        fields = ['nome', 'cpf', 'datanasc', 'endereco', 'cidade', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),  # Para tornar o campo de senha oculto
        }
