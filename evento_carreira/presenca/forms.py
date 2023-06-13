from django import forms
from presenca.models import Aluno

class CadastroPresencaForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_aluno', 'nome_professor']
