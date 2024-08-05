"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('animais/', AnimaisView.as_view(), name='animais'),
    path('autorizados/', AutorizadosView.as_view(),name='autorizados'),
    path('detalhes/', DetalhesView.as_view(),name='detalhes'),
    path('estoques/', EstoquesView.as_view(), name='estoques'),
    path('funcoes/', FuncoesView.as_view(),name='funcoes'),
    path('produtos/', ProdutosView.as_view(),name='produtos'),
    path('saidas/', SaidasView.as_view(),name='saidas'),
    path('setores/', SetoresView.as_view(),name='setores'),
]
