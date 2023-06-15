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

        self.assertEqual(response.status_code, 302)  # Verificando se foi redirecionado
        self.assertEqual(Aluno.objects.count(), 1)  # Verificando se um objeto Aluno foi criado
        aluno = Aluno.objects.first()
        self.assertEqual(aluno.nome_aluno, 'João Silva')  # Verificando o valor do campo nome_aluno
        self.assertEqual(aluno.nome_professor, 'Maria Souza')  # Verificando o valor do campo nome_professor

    def test_cadastro_presenca_get(self):
        response = self.client.get(reverse('cadastro_presenca'))

        self.assertEqual(response.status_code, 200)  # Verificando se a página foi carregada corretamente
        self.assertIsInstance(response.context['form'], CadastroPresencaForm)  # Verificando se o formulário é uma instância de CadastroPresencaForm


class ListarAlunosTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        # Criando alguns objetos Aluno para testar
        Aluno.objects.create(nome_aluno='João Silva', nome_professor='Maria Souza')
        Aluno.objects.create(nome_aluno='Pedro Santos', nome_professor='Ana Oliveira')

    def test_listar_alunos(self):
        # Fazendo uma solicitação GET usando o cliente de teste
        response = self.client.get(reverse('listar_alunos'))

        # Verificando o código de status HTTP retornado
        self.assertEqual(response.status_code, 200)

        # Verificando se a template correta está sendo usada
        self.assertTemplateUsed(response, 'listar_alunos.html')

        # Obtendo os objetos Aluno passados para a template no contexto
        alunos_contexto = response.context['alunos']

        # Verificando se os objetos Aluno são do tipo QuerySet
        self.assertIsInstance(alunos_contexto, QuerySet)

        # Verificando se a quantidade de objetos Aluno passados para a template está correta
        self.assertEqual(alunos_contexto.count(), 2)



class AlunoModelTestCase(TestCase):
    def test_campos_model(self):
        # Criando um objeto Aluno para teste
        aluno = Aluno.objects.create(
            nome_aluno='João Silva',
            nome_professor='Maria Souza'
        )

        # Verificando se os campos do modelo estão definidos corretamente
        self.assertEqual(aluno.nome_aluno, 'João Silva')
        self.assertEqual(aluno.nome_professor, 'Maria Souza')


class CadastroPresencaFormTestCase(TestCase):
    def test_form_valido(self):
        # Cria um dicionário com dados válidos
        dados_validos = {
            'nome_aluno': 'João Silva',
            'nome_professor': 'Maria Souza',
        }

        # Instancia o formulário com os dados válidos
        form = CadastroPresencaForm(data=dados_validos)

        # Verifica se o formulário é válido
        self.assertTrue(form.is_valid())

    def test_form_invalido(self):
        # Cria um dicionário com dados inválidos
        dados_invalidos = {
            'nome_aluno': '',  # Nome do aluno em branco (inválido)
            'nome_professor': 'Maria Souza',
        }

        # Instancia o formulário com os dados inválidos
        form = CadastroPresencaForm(data=dados_invalidos)

        # Verifica se o formulário é inválido
        self.assertFalse(form.is_valid())
