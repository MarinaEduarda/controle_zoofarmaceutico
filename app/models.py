from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipos de produtos")
    def __str__(self):
        return f"{self.nome}"
class Meta:
    verbose_name = "Produto"
    verbose_name_plural = "Produtos"

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name="Nome do produto")
    imagem = models.ImageField(verbose_name="imagem")
    medida = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="medida")
    unid_medida = models.CharField(max_length=2, verbose_name="unidade de medida")
    lote = models.IntegerField(verbose_name="lote")
    data_fabricacao = models.DateField(verbose_name="data de fabricação")
    data_validade = models.DateField(verbose_name="data de validade")
    def __str__(self):
        return f"{self.produto}, {self.imagem}, {self.medida}, {self.unid_medida}, {self.lote}, {self.data_fabricacao}, {self.data_validade}"

class Meta:
    verbose_name = "Estoque"
    verbose_name_plural = "Estoques"

class Setor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do setor")
    def __str__(self):
        return f"{self.nome}"

class Meta:
    verbose_name = "Setor"
    verbose_name_plural = "Setores"

class Animal(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Animais trabalhados")
    setor = models.ForeignKey(Setor,on_delete=models.CASCADE, verbose_name="Setor pertencente")

    def __str__(self):
        return f"{self.nome}, {self.setor}"

class Meta:
    verbose_name = "Animal"
    verbose_name_plural = "Animais"

class Funcao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Função")

    def __str__(self):
        return f"{self.nome}"

class Meta:
    verbose_name = "Funcao"
    verbose_name_plural = "Funcoes"

class Autorizado(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    CPF = models.IntegerField(verbose_name = "CPF")
    email = models.CharField(max_length=100, verbose_name="email")
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, verbose_name="Funcao")
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, verbose_name="Funcao")

    def __str__(self):
        return f"{self.nome}, {self.CPF}, {self.email}, {self.funcao}, {self.setor}"

class Meta:
    verbose_name = "Autorizado"
    verbose_name_plural = "Autorizados"

class Saida(models.Model):
    autorizado = models.ForeignKey(Setor,on_delete=models.CASCADE, verbose_name="Pessoa autorizada")
    data = models.DateField(verbose_name ="data da saida")
    horario = models.TimeField(verbose_name = "horario da saida")

    def __str__(self):
        return f"{self.autorizado}, {self.data}, {self.horario}"

class Meta:
    verbose_name = "Saida"
    verbose_name_plural = "Saidas"

class Detalhes(models.Model):
    saida = models.ForeignKey(Saida,on_delete=models.CASCADE, verbose_name="Saída referente")
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, verbose_name="Produto retirado")
    quantidade = models.IntegerField(verbose_name = "quantidade")
    unid_medida = models.CharField(max_length=2, verbose_name="unidade de medida")

    def __str__(self):
        return f"{self.saida}, {self.estoque}, {self.quantidade}, {self.unid_medida}"

class Meta:
    verbose_name = "Detalhes"
    verbose_name_plural = "Detalhes"



