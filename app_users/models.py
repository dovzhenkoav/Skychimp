from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    surname = models.CharField(max_length=50, verbose_name='отчество')

    comment = models.CharField(max_length=128, verbose_name='комментарий', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
