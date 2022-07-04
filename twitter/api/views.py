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
        new_user = TwitterUserService.create_user(request)
        serializer = self.get_serializer(new_user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=["post"], url_path='follow_user')
    def follow_user(self, request, pk=None):
        pass

      
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def create(self, request):
        was_saved = TweetService.create_tweet(request)
        if was_saved:
            serializer = TweetSerializer(was_saved)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else: 
            return Response({"error": "tweeter_user_id does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=False, methods=["get"], url_path='get_recent_tweets')
    def get_recent_tweetss(self, request):
        tweets_query = TweetService.list_recent_tweets(request.user)
        serializer = TweetSerializer(tweets_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path='get_users_tweets')
    def get_users_tweets(self, request):
        users_tweets = TweetService.find_users_tweets(request.data, request.user)
        if users_tweets:
            tweets = TweetSerializer(users_tweets, many=True)
            return Response(tweets.data, status=status.HTTP_200_OK)
        elif users_tweets == None: return Response({"error": "users selected dont have tweets asinged to them"}, status=status.HTTP_204_NO_CONTENT)
        else: return Response({"error": "users selected dont exist"}, status=status.HTTP_400_BAD_REQUEST)

        
    @action(detail=True, methods=["post"], url_path='like_tweet')
    def like_tweet(self, request, pk=None):
        updated_tweet = TweetService.like_tweet(pk, request.user)
        if updated_tweet:
            serializer = TweetSerializer(updated_tweet)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response({"error": "tweet selected dont exist"}, status=status.HTTP_400_BAD_REQUEST)

        
    @action(detail=True, methods=["post"], url_path='comment_tweet')
    def comment_tweet(self, request, pk=None):
        pass
