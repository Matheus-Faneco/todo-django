from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    name = models.CharField(
        db_column='tx_name',
        max_length=255,
        verbose_name='Nome',
    )
    email = models.CharField(
        db_column='tx_email',
        max_length=255,
        unique=True,
        verbose_name='Email',
    )
    password = models.CharField(
        db_column='tx_password',
        max_length=255,
        verbose_name='Senha',
    )
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
