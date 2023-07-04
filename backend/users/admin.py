from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from config.settings import PAGINATION_LIMIT_IN_ADMIN_PANEL
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
    ordering = ('-last_login',)
    empty_value_display = '-пусто-'
    list_per_page = PAGINATION_LIMIT_IN_ADMIN_PANEL

    @admin.display(description='Количество новостей')
    def get_news_count(self, obj):
        return obj.news.count()

    @admin.display(description='Количество лайков')
    def get_likes_count(self, obj):
        return obj.likes.count()

    @admin.display(description='Количество комментариев')
    def get_comments_count(self, obj):
        return obj.comments.count()
