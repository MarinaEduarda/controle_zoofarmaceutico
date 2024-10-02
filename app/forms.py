from django import forms  # Importa o módulo de formulários do Django
# Importa os modelos que serão utilizados nos formulários
from .models import Produto, Estoque, Setor, Animal, Usuario, Saida, Detalhes

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = '__all__'

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = '__all__'

class DetalhesForm(forms.ModelForm):
    class Meta:
        model = Detalhes
        fields = '__all__'
