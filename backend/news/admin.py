from django.contrib import admin
from django.contrib.auth.models import Group

from config.settings import PAGINATION_LIMIT_IN_ADMIN_PANEL
from .models import News, Comments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'text', 'author', 'pub_date',
        'get_likes_count', 'get_comments_count'
    )
    list_display_links = ('title',)
    search_fields = ('text',)
    list_filter = ('pub_date', 'author')
    ordering = ('-pub_date',)
    empty_value_display = '-пусто-'
    list_per_page = PAGINATION_LIMIT_IN_ADMIN_PANEL

    @admin.display(description='Количество лайков')
    def get_likes_count(self, obj):
        return obj.likes.count()

    @admin.display(description='Количество комментариев')
    def get_comments_count(self, obj):
        return obj.comments.count()


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'news', 'pub_date')
    list_display_links = ('author',)
    search_fields = ('text',)
    list_filter = ('pub_date', 'author')
    ordering = ('-pub_date',)
    empty_value_display = '-пусто-'
    list_per_page = PAGINATION_LIMIT_IN_ADMIN_PANEL


admin.site.unregister(Group)
