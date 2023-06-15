from django.test import TestCase, Client
from django.urls import reverse
from .models import Aluno
from .forms import CadastroPresencaForm
from django.db.models import QuerySet


class BaseTestCase(TestCase):
    def setUp(self):
        self.client = Client()


class CadastroPresencaTestCase(BaseTestCase):
    def test_cadastro_presenca_post(self):
        form_data = {
            'nome_aluno': 'João Silva',
            'nome_professor': 'Maria Souza'
        }
        response = self.client.post(reverse('cadastro_presenca'), data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Aluno.objects.count(), 1)
        aluno = Aluno.objects.first()
        self.assertEqual(aluno.nome_aluno, 'João Silva')
        self.assertEqual(aluno.nome_professor, 'Maria Souza')

    def test_cadastro_presenca_get(self):
        response = self.client.get(reverse('cadastro_presenca'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CadastroPresencaForm)


class ListarAlunosTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        Aluno.objects.create(nome_aluno='João Silva', nome_professor='Maria Souza')
        Aluno.objects.create(nome_aluno='Pedro Santos', nome_professor='Ana Oliveira')

    def test_listar_alunos(self):
        response = self.client.get(reverse('listar_alunos'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'listar_alunos.html')

        alunos_contexto = response.context['alunos']

        self.assertIsInstance(alunos_contexto, QuerySet)

        self.assertEqual(alunos_contexto.count(), 2)



class AlunoModelTestCase(TestCase):
    def test_campos_model(self):
        aluno = Aluno.objects.create(
            nome_aluno='João Silva',
            nome_professor='Maria Souza'
        )

        self.assertEqual(aluno.nome_aluno, 'João Silva')
        self.assertEqual(aluno.nome_professor, 'Maria Souza')


class CadastroPresencaFormTestCase(TestCase):
    def test_form_valido(self):
        dados_validos = {
            'nome_aluno': 'João Silva',
            'nome_professor': 'Maria Souza',
        }

        form = CadastroPresencaForm(data=dados_validos)

        self.assertTrue(form.is_valid())

    def test_form_invalido(self):
        dados_invalidos = {
            'nome_aluno': '',
            'nome_professor': 'Maria Souza',
        }

        form = CadastroPresencaForm(data=dados_invalidos)

        self.assertFalse(form.is_valid())
