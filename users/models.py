from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    username = models.CharField(verbose_name='Имя', max_length=25, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
