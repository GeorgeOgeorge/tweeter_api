from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from ..models import Tweet, TwitterUser
from .serializers import TweetSerializer, TwitterUserSerializer

class TwitterUserViewSet(viewsets.ModelViewSet):
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TwitterUser.create_user(serializer, request.data['password'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

      
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    @action(detail=False, methods=["get"], url_path='get_recent_tweets')
    def get_recent_tweetss(self, request):
        tweets_query = Tweet.objects.all().order_by('-created')[:10]
        tweets = TweetSerializer(tweets_query, many=True)
        return Response(tweets.data, status=status.HTTP_200_OK)
        