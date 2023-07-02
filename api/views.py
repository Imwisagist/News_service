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
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        url_path='like',
        methods=('POST', 'DELETE'),
        detail=True,
    )
    def set_like(self, request, pk):
        news = get_object_or_404(News, id=pk)
        if request.method == 'POST':
            news.likes.add(request.user)
            return Response(
                NewsSerializer(news).data,
                status=status.HTTP_201_CREATED
            )

        if request.method == 'DELETE':
            news.likes.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


class GetAuthToken(ObtainAuthToken):
    authentication_classes = []


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_news(self):
        return get_object_or_404(News, pk=self.kwargs.get('news_id'))

    def get_queryset(self):
        return self.get_news().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, news=self.get_news())
