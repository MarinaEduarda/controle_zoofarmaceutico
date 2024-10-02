from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from django.views import View
from django.contrib import messages
from .forms import ProdutoForm, EstoqueForm, AnimalForm, SetorForm, UsuarioForm, SaidaForm, DetalhesForm

# Create your views here.

# VISUALIZAÇÃO DE TABELAS

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class ProdutosView(View):
    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all()
        return render(request, 'produto.html', {'produtos': produtos})

class EstoquesView(View):
    def get(self, request, *args, **kwargs):
        estoques = Estoque.objects.all()
        return render(request, 'estoque.html', {'estoques': estoques})

class AnimaisView(View):
    def get(self, request, *args, **kwargs):
        animais = Animal.objects.all()
        return render(request, 'animal.html', {'animais': animais})

class SetoresView(View):
    def get(self, request, *args, **kwargs):
        setores = Setor.objects.all()
        return render(request, 'setor.html', {'setores': setores})

class UsuariosView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})

class SaidasView(View):
    def get(self, request, *args, **kwargs):
        saidas = Saida.objects.all()
        return render(request, 'saida.html', {'saidas': saidas})

class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        detalhes = Detalhes.objects.all()
        return render(request, 'detalhes.html', {'detalhes': detalhes})

## DELETE
class DeleteProdutoView(View):
    def get(self, request, id, *args, **kwargs):
        produto = get_object_or_404(Produto, id=id)
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('produto')

class DeleteEstoqueView(View):
    def get(self, request, id, *args, **kwargs):
        estoque = get_object_or_404(Estoque, id=id)
        estoque.delete()
        messages.success(request, 'Estoque excluído com sucesso!')
        return redirect('estoque')

class DeleteAnimalView(View):
    def get(self, request, id, *args, **kwargs):
        animal = get_object_or_404(Animal, id=id)
        animal.delete()
        messages.success(request, 'Animal excluído com sucesso!')
        return redirect('animal')

class DeleteSetorView(View):
    def get(self, request, id, *args, **kwargs):
        setor = get_object_or_404(Setor, id=id)
        setor.delete()
        messages.success(request, 'Setor excluído com sucesso!')
        return redirect('setor')

class DeleteUsuarioView(View):
    def get(self, request, id, *args, **kwargs):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.delete()
        messages.success(request, 'Usuário excluído com sucesso!')
        return redirect('usuario')

class DeleteSaidaView(View):
    def get(self, request, id, *args, **kwargs):
        saida = get_object_or_404(Saida, id=id)
        saida.delete()
        messages.success(request, 'Saída excluída com sucesso!')
        return redirect('saida')

class DeleteDetalhesView(View):
    def get(self, request, id, *args, **kwargs):
        detalhe = get_object_or_404(Detalhes, id=id)
        detalhe.delete()
        messages.success(request, 'Detalhe de saída excluído com sucesso!')
        return redirect(reverse('detalhes'))

## EDIÇÃO DAS TABELAS ###

class EditarProdutoView(View):
    template_name = 'editar_produto.html'
    
    def get(self, request, id, *args, **kwargs):
        produto = get_object_or_404(Produto, id=id)
        form = ProdutoForm(instance=produto)
        return render(request, self.template_name, {'produto': produto, 'form': form})

    def post(self, request, id, *args, **kwargs):
        produto = get_object_or_404(Produto, id=id)
        form = ProdutoForm(request.POST, instance=produto)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect(reverse('produto')) # Redirecionar de volta para a página de edição
        
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'produto': produto, 'form': form})


class EditarEstoqueView(View):
    template_name = 'editar_estoque.html'
    
    def get(self, request, id, *args, **kwargs):
        estoque = get_object_or_404(Estoque, id=id)
        form = EstoqueForm(instance=estoque)
        return render(request, self.template_name, {'estoque': estoque, 'form': form})

    def post(self, request, id, *args, **kwargs):
        estoque = get_object_or_404(Estoque, id=id)
        form = EstoqueForm(request.POST, instance=estoque)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect(reverse('estoque')) # Redirecionar de volta para a página de edição
        
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'estoque': estoque, 'form': form})
        

class EditarUsuarioView(View):
    template_name = 'editar_usuario.html'
    
    def get(self, request, id, *args, **kwargs):
        usuario = get_object_or_404(Usuario, id=id)
        form = UsuarioForm(instance=usuario)
        return render(request, self.template_name, {'usuario': usuario, 'form': form})

    def post(self, request, id, *args, **kwargs):
        usuario = get_object_or_404(Usuario, id=id)
        form = UsuarioForm(request.POST, instance=usuario)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect(reverse('usuario')) # Redirecionar de volta para a página de edição
        
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'usuario': usuario, 'form': form})


class EditarSetorView(View):
    template_name = 'editar_setor.html'
    
    def get(self, request, id, *args, **kwargs):
        setor = get_object_or_404(Setor, id=id)
        form = SetorForm(instance=setor)
        return render(request, self.template_name, {'setor': setor, 'form': form})

    def post(self, request, id, *args, **kwargs):
        setor = get_object_or_404(Setor, id=id)
        form = SetorForm(request.POST, instance=setor)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect(reverse('setor')) # Redirecionar de volta para a página de edição
        
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'setor': setor, 'form': form})


class EditarAnimalView(View):
    template_name = 'editar_animal.html'
    
    def get(self, request, id, *args, **kwargs):
        animal = get_object_or_404(Animal, id=id)
        form = AnimalForm(instance=animal)
        return render(request, self.template_name, {'animal': animal, 'form': form})

    def post(self, request, id, *args, **kwargs):
        animal = get_object_or_404(Animal, id=id)
        form = AnimalForm(request.POST, instance=animal)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect(reverse('animal')) # Redirecionar de volta para a página de edição
        
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'animal': animal, 'form': form})

class EditarSaidaView(View):
    template_name = 'editar_saida.html'
    
    def get(self, request, id, *args, **kwargs):
        saida = get_object_or_404(Saida, id=id)
        form = SaidaForm(instance=saida)
        return render(request, self.template_name, {'saida': saida, 'form': form})

    def post(self, request, id, *args, **kwargs):
        saida = get_object_or_404(Saida, id=id)
        form = SaidaForm(request.POST, instance=saida)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect(reverse('saida')) # Redirecionar de volta para a página de edição
        
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'saida': saida, 'form': form})

class EditarDetalhesView(View):
    template_name = 'editar_detalhes.html'
    
    def get(self, request, id, *args, **kwargs):
        detalhes = get_object_or_404(Detalhes, id=id)
        form = DetalhesForm(instance=detalhes)
        return render(request, self.template_name, {'detalhes': detalhes, 'form': form})

    def post(self, request, id, *args, **kwargs):
        detalhes = get_object_or_404(Detalhes, id=id)
        form = DetalhesForm(request.POST, instance=detalhes)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect(reverse('detalhes')) # Redirecionar de volta para a página de edição
        
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'detalhes': detalhes, 'form': form})
