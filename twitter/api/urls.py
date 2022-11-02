from django.urls import path
from rest_framework.routers import DefaultRouter

from twitter.api.views import (
    TweetViewSet, TwitterUserViewSet,
    get_tweet_comments
)


router = DefaultRouter()
router.register(r'twitterusers', TwitterUserViewSet, basename='twitterusers')
router.register(r'tweets', TweetViewSet, basename='tweets')

urlpatterns = [
    path('tweets/<int:pk>/get_tweet_comments', get_tweet_comments)
]

urlpatterns += router.urls