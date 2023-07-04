from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Users(AbstractUser):
    username = models.CharField(
        'Имя',
        max_length=25,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Имя пользователя содержит недопустимый символ'
        )]
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
