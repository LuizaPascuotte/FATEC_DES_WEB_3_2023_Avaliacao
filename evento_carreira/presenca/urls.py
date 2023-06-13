from presenca import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.cadastro_presenca, name='cadastro_presenca'),
    path('listar/', views.listar_alunos, name='listar_alunos'),
]