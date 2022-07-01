from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from ..models import Tweet, TwitterUser
from ..service import TwitterUserService, TweetService

from .serializers import TweetSerializer, TwitterUserSerializer

class TwitterUserViewSet(viewsets.ModelViewSet):
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TwitterUserService.create_user(serializer, request.data['password'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=["post"], url_path='follow_user')
    def follow_user(self, request, pk=None):
        pass

      
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        was_saved = TweetService.create_tweet(serializer, request.data['tweet_op'])
        if was_saved:
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else: 
            return Response({"error": "tweeter_user_id does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=False, methods=["get"], url_path='get_recent_tweets')
    def get_recent_tweetss(self, request):
        tweets_query = TweetService.list_recent_tweets()
        tweets = TweetSerializer(tweets_query, many=True)
        return Response(tweets.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path='get_users_tweets')
    def get_users_tweets(self, request):
        users_tweets = TweetService.find_users_tweets(request.data)
        if users_tweets:
            tweets = TweetSerializer(users_tweets, many=True)
            return Response(tweets.data, status=status.HTTP_200_OK)
        elif users_tweets == None: Response({"error": "users selected dont have tweets asinged to them"}, status=status.HTTP_204_NO_CONTENT)
        else: Response({"error": "users selected dont exist"}, status=status.HTTP_400_BAD_REQUEST)

        
    @action(detail=True, methods=["post"], url_path='like_tweet')
    def like_tweet(self, request, pk=None):
        pass

    @action(detail=True, methods=["post"], url_path='comment_tweet')
    def comment_tweet(self, request, pk=None):
        pass
