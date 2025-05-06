from random import choices

from django.db import models

class Task(models.Model):

    title = models.CharField(
        db_column='tx_title',
        max_length=200,
        verbose_name='Titulo',
    )
    description = models.TextField(
        db_column='tx_description',
        max_length=500,
        verbose_name='Descrição'
    )
    responsible = models.CharField(
        db_column='tx_responsible',
        max_length=100,
        verbose_name='Responsável'
    )
    PRIORITY_CHOICES = [
        ('L', 'Baixa'),
        ('M', 'Média'),
        ('H', 'Alta'),
    ]
    priority = models.CharField(
        db_column='tx_priority',
        max_length=1,
        choices=PRIORITY_CHOICES,
        verbose_name='Prioridade'
    )

    def __str__(self):
        return self.title

