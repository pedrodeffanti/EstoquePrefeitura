from django.db import models

class itemModels(models.Model):
    Item = models.CharField('Ítem: ', max_length=50)
    Quant = models.PositiveIntegerField('Quantidade: ')

    def __str__(self):
        return str(self.Item)

    class Meta:
        verbose_name = 'Ítem'
        verbose_name_plural = 'Ítens'

class ativoModels(models.Model):
    Ativo = models.CharField('Nome do Ativo: ', max_length=25)
    Resp = models.CharField('Responsável: ', max_length=100)

    def __str__(self):
        return str(self.Ativo)

    class Meta:
        verbose_name = 'Ativo'
        verbose_name_plural = 'Ativos'

class saidaModels(models.Model):
    data = models.DateField('Data')
    ativo = models.ForeignKey(ativoModels, verbose_name='Ativo', on_delete=models.CASCADE)
    item = models.ForeignKey(itemModels, verbose_name='Ítem', on_delete=models.CASCADE)
    quant = models.PositiveIntegerField('Quantidade')

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = 'Saida'
        verbose_name_plural = 'Saídas'