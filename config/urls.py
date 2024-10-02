from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),  # Página inicial usando TemplateView
    path('index/', IndexView.as_view(), name='index'),  # Página inicial usando IndexView

    # PRODUTO
    path('produto/', ProdutosView.as_view(), name='produto'),
    path('produto/delete/<int:id>/', DeleteProdutoView.as_view(), name='delete_produto'),  # Exclusão de produtos
    path('produto/editar/<int:id>/', EditarProdutoView.as_view(), name='editar_produto'),  # Correção do redirecionamento aqui
    
    # ESTOQUE
    path('estoque/', EstoquesView.as_view(), name='estoque'),
    path('estoque/delete/<int:id>/', DeleteEstoqueView.as_view(), name='delete_estoque'),  # Exclusão de estoques
    path('estoque/editar/<int:id>/', EditarEstoqueView.as_view(), name='editar_estoque'),
    
    # ANIMAL 
    path('animal/', AnimaisView.as_view(), name='animal'),
    path('animal/delete/<int:id>/', DeleteAnimalView.as_view(), name='delete_animal'),  # Exclusão de animais
    path('animal/editar/<int:id>/', EditarAnimalView.as_view(), name='editar_animal'),
    
    # SETOR
    path('setor/', SetoresView.as_view(), name='setor'),
    path('setor/delete/<int:id>/', DeleteSetorView.as_view(), name='delete_setor'),  # Exclusão de setores
    path('setor/editar/<int:id>/', EditarSetorView.as_view(), name='editar_setor'),
   
    # USUARIO
    path('usuario/', UsuariosView.as_view(), name='usuario'),
    path('usuario/delete/<int:id>/', DeleteUsuarioView.as_view(), name='delete_usuario'),  # Exclusão de usuários
    path('usuario/editar/<int:id>/', EditarUsuarioView.as_view(), name='editar_usuario'),
    
    # SAIDA
    path('saida/', SaidasView.as_view(), name='saida'),
    path('saida/delete/<int:id>/', DeleteSaidaView.as_view(), name='delete_saida'),  # Exclusão de saídas
    path('saida/editar/<int:id>/', EditarSaidaView.as_view(), name='editar_saida'),
    
    # DETALHES
    path('detalhes/', DetalhesView.as_view(), name='detalhes'),
    path('detalhes/delete/<int:id>/', DeleteDetalhesView.as_view(), name='delete_detalhes'),  # Exclusão de detalhes
    path('detalhes/editar/<int:id>/', EditarDetalhesView.as_view(), name='editar_detalhes'),
]
