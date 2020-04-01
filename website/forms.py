from django import forms
from projectWebsite.models import Funcionario


class InsereFuncionarioForm(forms.ModelForm):
    """ Employee insertion form"""

    # Checkbox to mark if it's boss
    chefe = forms.BooleanField(label='Chefe?', required=False)

    # TextArea to insert biography
    biografia = forms.CharField(label='Biografia', required=False,
                                widget=forms.Textarea)

    class Meta:

        # Base model
        model = Funcionario

        # Fields that will be in the form
        fields = ['nome', 'sobrenome', 'cpf', 'tempo_de_servico',
                  'remuneracao']

        # Fields that will not be in the form
        exclude = []
