from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.authtoken.models import Token

User = get_user_model()

LIMIT_CHARS = 25


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(
        User, verbose_name='Автор',
        on_delete=models.CASCADE, related_name='news',
    )
    likes = models.ManyToManyField(
        User, verbose_name='Лайки',
        related_name='likes', blank=True
    )
    pub_date = models.DateField(
        verbose_name='Дата публикации', auto_now=True,
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title[:LIMIT_CHARS]


class Comments(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    news = models.ForeignKey(
        News, on_delete=models.CASCADE,
        verbose_name='Заголовок новости', related_name='comments',
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор комментария', related_name='comments',
    )
    pub_date = models.DateField(
        verbose_name='Дата публикации', auto_now_add=True,
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:LIMIT_CHARS]
