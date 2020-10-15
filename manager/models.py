from django.db import models

# Create your models here.

class Base(models.Model):
    criados = models.DateTimeField('Criação', auto_now_add=True)
    modificado = models.DateTimeField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Funcao(Base):
    funcao = models.CharField('Função', max_length=200)

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = "Funções"

    def __str__(self):
        return self.funcao