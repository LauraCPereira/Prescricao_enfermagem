from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.Autenticacao.as_view()),
url(r'^tarefas/criar/', views.CriarTarefas.as_view(), name='nova-tarefa'),
url(r'^sair/', views.sair)

]
