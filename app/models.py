from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de produto")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name="Nome do produto")
    imagem = models.ImageField(verbose_name="Imagem")
    medida = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Medida")
    unid_medida = models.CharField(max_length=2, verbose_name="Unidade de medida")
    lote = models.CharField(max_length=100,verbose_name="Lote")
    data_fabricacao = models.DateField(verbose_name="Data de fabricação")
    data_validade = models.DateField(verbose_name="Data de validade")
    quantidade = models.IntegerField(verbose_name = "Quantidade",  default= 0)

    def __str__(self):
        return f"{self.produto}, {self.imagem}, {self.medida}, {self.unid_medida}, {self.lote}, {self.data_fabricacao}, {self.data_validade}, {self.quantidade}"

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"

class Setor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do setor")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"

class Animal(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do animal")
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, verbose_name="Setor pertencente")

    def __str__(self):
        return f"{self.nome}, {self.setor}"

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"

class Funcao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Função")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Função"
        verbose_name_plural = "Funções"

class Autorizado(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    CPF = models.CharField(max_length=100, verbose_name="CPF")
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, verbose_name="Função")
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, verbose_name="Setor")
    email = models.CharField(max_length=100, verbose_name="Email")
    senha = models.CharField(max_length=100, verbose_name="Senha", default='ifsuldeminas')

    def __str__(self):
        return f"{self.nome}, {self.CPF}, {self.funcao}, {self.setor}, {self.email}, {self.senha}"

    class Meta:
        verbose_name = "Autorizado"
        verbose_name_plural = "Autorizados"

class Saida(models.Model):
    autorizado = models.ForeignKey(Autorizado, on_delete=models.CASCADE, verbose_name="Pessoa autorizada")
    data = models.DateField(verbose_name="Data da saída")
    horario = models.TimeField(verbose_name="Horário da saída")

    def __str__(self):
        return f"{self.autorizado}, {self.data}, {self.horario}"

    class Meta:
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"

class Detalhes(models.Model):
    saida = models.ForeignKey(Saida, on_delete=models.CASCADE, verbose_name="Saída referente")
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, verbose_name="Produto retirado")
    quantidade = models.IntegerField(verbose_name="Quantidade")

    def __str__(self):
        return f"{self.saida}, {self.estoque}, {self.quantidade}"

    class Meta:
        verbose_name = "Detalhe"
        verbose_name_plural = "Detalhes"
