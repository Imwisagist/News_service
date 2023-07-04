from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from news.models import News, Comments
from .permissions import IsAuthorOrReadOnly
from .serializers import NewsSerializer, CommentSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all().select_related(
        'author').prefetch_related('likes', 'comments').annotate(
        likes_count=Count('likes'), comments_count=Count('comments'),
    )
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        url_path='like',
        methods=('POST',),
        detail=True,
    )
    def set_like(self, request, pk):
        get_object_or_404(News, id=pk).likes.add(request.user)
        return Response(status=status.HTTP_201_CREATED)

    @set_like.mapping.delete
    def delete_like(self, request, pk):
        get_object_or_404(News, id=pk).likes.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetAuthToken(ObtainAuthToken):
    authentication_classes = []


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all().select_related('author', 'news')
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_news(self):
        return get_object_or_404(News, pk=self.kwargs.get('news_id'))

    def get_queryset(self):
        return self.get_news().comments.all().select_related('author', 'news')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, news=self.get_news())

    @action(
        methods=('DELETE',),
        detail=True,
    )
    def delete_comment(self, request, pk):
        get_object_or_404(Comments, id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
