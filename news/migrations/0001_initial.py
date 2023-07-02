from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('pub_date', models.DateField(auto_now=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Лайки')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
                'ordering': ('pub_date',),
            },
        ),
    ]
