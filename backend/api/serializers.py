from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from news.models import News, Comments


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'pub_date', 'text', 'news', 'author']
        read_only_fields = ('news',)


class NewsSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    last_ten_comments = serializers.SerializerMethodField()

    @staticmethod
    def get_likes_count(obj):
        return obj.likes.count()

    @staticmethod
    def get_comments_count(obj):
        return obj.comments.count()

    @staticmethod
    def get_last_ten_comments(obj):
        return (str(t) for t in obj.comments.all().order_by('-id')[:10])

    class Meta:
        model = News
        ordering = ('pub_date',)
        fields = [
            'id', 'pub_date', 'title', 'text',
            'author', 'likes_count', 'comments_count', 'last_ten_comments'
        ]
