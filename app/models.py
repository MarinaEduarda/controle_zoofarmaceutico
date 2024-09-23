from django.db import models
from django.db.models import Sum, F, DecimalField
from django.core.exceptions import ValidationError

class Setor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Setor")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"


class Produto(models.Model):
    UNIDADES_DE_MEDIDA = (
        (1, 'Unidade'),
        (2, 'mL'),
    )

    nome = models.CharField(max_length=100, verbose_name="Nome")
    quantidade_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantidade Total", default=0 )
    unid_medida = models.IntegerField(verbose_name="Unidade de Medida", choices=UNIDADES_DE_MEDIDA)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, verbose_name="Setor Pertencente")

    def __str__(self):
        return f"{self.nome}, {self.quantidade_total}, {self.get_unid_medida_display()}, {self.setor}"

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def atualizar_quantidade_total(self):
        """
        Atualiza a quantidade_total do produto com base nas entradas de estoque
        (quantidade * quantidade_frascos) e nas saídas detalhadas.
        """
        # Soma das quantidades dos estoques multiplicadas pela quantidade_frascos
        total_estoque = self.estoques.aggregate(total=Sum(F('quantidade') * F('quantidade_frascos'), output_field=DecimalField()))['total'] or 0

        # Soma das quantidades dos detalhes (saídas)
        total_detalhes = self.detalhes.aggregate(total=Sum('quantidade'))['total'] or 0

        # Atualiza a quantidade_total
        self.quantidade_total = total_estoque - total_detalhes
        self.save(update_fields=['quantidade_total'])


class Estoque(models.Model):
    UNIDADES_DE_MEDIDA = (
        (1, 'Unidade'),
        (2, 'mL'),
    )

    produto = models.ForeignKey(Produto,related_name='estoques',on_delete=models.CASCADE,verbose_name="Produto")
    lote = models.CharField(max_length=100, verbose_name="Lote")
    data_fabricacao = models.DateField(verbose_name="Data de Fabricação")
    data_validade = models.DateField(verbose_name="Data de Validade")
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantidade")
    unid_medida = models.IntegerField(verbose_name="Unidade de Medida", choices=UNIDADES_DE_MEDIDA)
    quantidade_frascos = models.IntegerField(verbose_name="Quantidade de Frascos", default=0)

    def __str__(self):
        return f"{self.produto}, {self.lote}, {self.data_fabricacao}, {self.data_validade}, {self.quantidade}, {self.get_unid_medida_display()}, {self.quantidade_frascos}"

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"

    def save(self, *args, **kwargs):
        # Se a unidade de medida não for 'mL', define quantidade_frascos como 1
        if self.unid_medida != 2:
            self.quantidade_frascos = 1

        super().save(*args, **kwargs)

        # Atualiza a quantidade_total do produto após salvar
        self.produto.atualizar_quantidade_total()


class Animal(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Animal")
    especie = models.CharField(max_length=100, verbose_name="Espécie")
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, verbose_name="Setor Pertencente")

    def __str__(self):
        return f"{self.nome}, {self.especie}, {self.setor}"

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"


class Usuario(models.Model):
    FUNCAO= (
        (1, 'Coordenador'),
        (2, 'Aluno Morador'),
        (3, 'Funcionário'),
    )
    PERFIL= (
        (1, 'Administrador'),
        (2, 'Usuário'),
        (3, 'Gerenciador'),
    )

    nome = models.CharField(max_length=100, verbose_name="Nome")
    CPF = models.CharField(max_length=14, verbose_name="CPF")  # Formato: XXX.XXX.XXX-XX
    email = models.EmailField(max_length=254, verbose_name="Email")
    funcao = models.IntegerField(verbose_name="Função", choices=FUNCAO)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, verbose_name="Setor")
    perfil = models.IntegerField(verbose_name="Tipo de Usuário", choices=PERFIL)
    senha = models.CharField(max_length=15, verbose_name="Senha", default='ifsuldeminas')  # Recomenda-se usar hashing para senhas

    def __str__(self):
        return f"{self.nome}, {self.CPF}, {self.email}, {self.get_funcao_display()}, {self.setor}, {self.perfil}"

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Saida(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    data = models.DateField(verbose_name="Data da Saída")
    horario = models.TimeField(verbose_name="Horário da Saída")

    def __str__(self):
        return f"{self.usuario}, {self.animal}, {self.data}, {self.horario}"

    class Meta:
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"


class Detalhes(models.Model):
    UNIDADES_DE_MEDIDA = (
        (1, 'Unidade'),
        (2, 'mL'),
    )

    saida = models.ForeignKey(Saida, on_delete=models.CASCADE, verbose_name="Saída Referente")
    produto = models.ForeignKey(Produto, related_name='detalhes', on_delete=models.CASCADE, verbose_name="Produto Retirado")
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantidade")
    unid_medida = models.IntegerField(verbose_name="Unidade de Medida", choices=UNIDADES_DE_MEDIDA)

    def __str__(self):
        return f"{self.saida}, {self.produto}, {self.quantidade}, {self.get_unid_medida_display()}"

    class Meta:
        verbose_name = "Detalhe"
        verbose_name_plural = "Detalhes"

    def clean(self):
        """
        Valida se a quantidade a ser retirada não excede a quantidade disponível.
        """
        if self.pk:
            # Se o objeto já existe (atualização), calcula a diferença
            original = Detalhes.objects.get(pk=self.pk)
            delta = self.quantidade - original.quantidade
        else:
            # Se é uma criação, delta é a quantidade
            delta = self.quantidade

        # Calcula a quantidade disponível antes da alteração
        quantidade_disponivel = self.produto.quantidade_total

        # Verifica se a quantidade retirada excede o estoque disponível
        if quantidade_disponivel - delta < 0:
            raise ValidationError('A quantidade retirada excede o estoque disponível.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        # Atualiza a quantidade_total do produto após salvar
        self.produto.atualizar_quantidade_total()
