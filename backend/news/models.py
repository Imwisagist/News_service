from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

LIMIT_CHARS = 25


class AbstractBaseModel(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateField('Дата публикации', auto_now=True)

    class Meta:
        abstract = True


class News(AbstractBaseModel):
    title = models.CharField(
        'Заголовок',
        max_length=100,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='news',
    )
    likes = models.ManyToManyField(
        User,
        verbose_name='Лайки',
        related_name='likes',
        blank=True,
    )

    class Meta:
        ordering = ('-pub_date', '-id')
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title[:LIMIT_CHARS]


class Comments(AbstractBaseModel):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Заголовок новости',
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments',
    )

    class Meta:
        ordering = ('pub_date', 'id')
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:LIMIT_CHARS]
