from django.urls import path
from rest_framework.routers import DefaultRouter

from twitter.api.views import (
    TweetViewSet, TwitterUserViewSet,
    get_users_tweets
)


router = DefaultRouter()
router.register(r'twitterusers', TwitterUserViewSet, basename='twitterusers')
router.register(r'tweets', TweetViewSet, basename='tweets')

urlpatterns = [
    path('tweets/<int:pk>/get_users_tweets', get_users_tweets)
]

urlpatterns += router.urls