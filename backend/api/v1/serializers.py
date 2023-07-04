from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from news.models import News, Comments


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'pub_date', 'text', 'news', 'author')
        read_only_fields = ('news',)


class NewsSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
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
        ordering = ('pub_date',)
        fields = (
            'id', 'pub_date', 'title', 'text', 'author',
            'likes_count', 'comments_count', 'ten_latest_comments',
        )
