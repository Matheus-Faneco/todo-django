from random import choices

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    responsible = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=[('L', 'Baixa'), ('M', 'Média'), ('H', 'Alta')])

    def __str__(self):
        return self.title

