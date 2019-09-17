from django.urls import path
from . import IndexTemplateView, FuncionarioListView, FuncionarioUpdateView,\
    FuncionarioDeleteView, FuncionarioCreateView


app_name = 'website'

# urlpatterns contains the URL routing list
urlpatterns = [
    # GET /
    path('', IndexTemplateView(), name='index'),

    # GET /funcionarios
    path('funcionarios/', FuncionarioListView.as_view(),
         name='lista_funcionarios'),

    # GET/POST /funcionario/{pk}
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(),
         name='atualiza_funcionario'),

    # GET/POST /funcionario/excluir/{pk}
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(),
         name='deleta_funcionario'),

    # GET /funcionario/cadastrar
    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(),
         name='cadastra_funcionario')
]
