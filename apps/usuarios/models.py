from django.db import models


class Usuario(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )
    email = models.EmailField(
        verbose_name='E-mail',
        unique=True,
    )
    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=20,
    )
    cpf = models.CharField(
        verbose_name='CPF',
        max_length=14,
        unique=True,
    )
    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento',
    )
    ativo = models.BooleanField(
        verbose_name='Ativo',
        default=True,
    )
    criado_em = models.DateTimeField(
        verbose_name='Criado em ',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.nome}'