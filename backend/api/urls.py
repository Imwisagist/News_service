from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewsViewSet, CommentsViewSet, GetAuthToken

router_v1 = DefaultRouter()
router_v1.register('news', NewsViewSet, basename='news')
router_v1.register(
    r'news/(?P<news_id>\d+)/comments', CommentsViewSet, basename='comments'
)

urlpatterns = [
    path('auth/', GetAuthToken.as_view()),
    path('', include(router_v1.urls)),
]
