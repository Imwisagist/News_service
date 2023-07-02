from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Users


@admin.register(Users)
class UsersAdmin(BaseUserAdmin):
    list_display = (
        'id', 'username', 'email', 'first_name', 'last_name', 'last_login',
        'date_joined', 'get_news_count', 'get_likes_count', 'get_comments_count'
    )
    list_display_links = ('username',)
    search_fields = ('username', 'email')
    list_filter = ('date_joined', 'last_login')
    ordering = ('last_login',)
    empty_value_display = '-пусто-'

    def get_news_count(self, obj):
        return obj.news.count()

    get_news_count.short_description = 'Количество новостей'

    def get_likes_count(self, obj):
        return obj.likes.count()

    get_likes_count.short_description = 'Количество лайков'

    def get_comments_count(self, obj):
        return obj.comments.count()

    get_comments_count.short_description = 'Количество комментариев'
