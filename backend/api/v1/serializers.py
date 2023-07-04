from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from news.models import News, Comments


class AbstractBaseSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)


class CommentSerializer(AbstractBaseSerializer):
    news = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Comments
        ordering = ('pub_date', 'id')
        fields = ('id', 'news', 'author', 'pub_date', 'text')


class NewsSerializer(AbstractBaseSerializer):
    likes_count = serializers.ReadOnlyField(source='likes.count')
    comments_count = serializers.ReadOnlyField(source='comments.count')
    ten_latest_comments = serializers.SerializerMethodField()

    @staticmethod
    def get_ten_latest_comments(obj):
        return (
            str(text) for text in
            obj.comments.all().order_by('-pub_date', '-id')[:10]
        )

    class Meta:
        model = News
        ordering = ('-pub_date', '-id')
        fields = (
            'id', 'title', 'author', 'pub_date', 'text', 'likes_count',
            'comments_count', 'ten_latest_comments',
        )
