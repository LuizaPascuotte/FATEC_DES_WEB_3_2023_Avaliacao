from django.shortcuts import render, redirect
from presenca.models import Aluno
from presenca.forms import CadastroPresencaForm

def cadastro_presenca(request):
    if request.method == 'POST':
        form = CadastroPresencaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_presenca')
    else:
        form = CadastroPresencaForm()
    return render(request, 'cadastro_presenca.html', {'form': form})

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})
