from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView,\
    DeleteView, CreateView
from projectWebsite.models import Funcionario
from website.forms import InsereFuncionarioForm


class IndexTemplateView(TemplateView):
    """ Main page"""

    template_name = 'website/index.html'


class FuncionarioListView(ListView):
    """ Funcionario List"""

    template_name = 'website/lista.html'
    model = Funcionario
    context_object_name = 'funcionarios'


class FuncionarioUpdateView(UpdateView):
    """ Funcionario Update"""

    template_name = 'website/atualiza.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy('website:lista_funcionarios')


class FuncionarioDeleteView(DeleteView):
    """ Funcionario Delete"""

    template_name = 'website/exclui.html'
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy('website:lista_funcionarios')


class FuncionarioCreateView(CreateView):
    """ Funcionario Registration"""

    template_name = 'website/cria.html'
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy('website:lista_funcionarios')
