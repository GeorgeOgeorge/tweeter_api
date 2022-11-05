from django.urls import path
from rest_framework.routers import DefaultRouter

from twitter.api.views import TweetViewSet, TwitterUserViewSet


router = DefaultRouter()
router.register(r'twitterusers', TwitterUserViewSet, basename='twitterusers')
router.register(r'tweets', TweetViewSet, basename='tweets')

urlpatterns = []
urlpatterns += router.urls