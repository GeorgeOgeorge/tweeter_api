from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from twitter.api.serializers import TweetSerializer, TwitterUserSerializer
from twitter.models import Tweet, TwitterUser
from twitter.service import TweetService, TwitterUserService


class TwitterUserViewSet(viewsets.ModelViewSet):
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer

    def create(self, request):
        new_user = TwitterUserService.create_user(request)
        serializer = self.get_serializer(new_user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["post"], url_path='login')
    def login(self, request):
        user_id = TwitterUserService.login(request)
        if user_id:
            return Response({"user_id": user_id}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "erro no login"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['POST'], url_path='username_exist')
    def username_exist(self, request):
        result = TwitterUserService.username_exists(request.data.get('name'))
        if result:
            return Response({"msg": "user exists"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"msg": "user not found"}, status=status.HTTP_200_OK)

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-created')
    serializer_class = TweetSerializer

    def create(self, request):
        user = TwitterUserService.find_user_by_id(int(request.data.get('user_id'))).first()
        was_saved = TweetService.create_tweet(request, user)
        if was_saved:
            serializer = TweetSerializer(was_saved)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"error": "tweeter_user_id does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path='get_recent_tweets')
    def get_recent_tweetss(self, request):
        user = TwitterUserService.find_user_by_id(int(request.data.get('user_id'))).first()
        tweets_query = TweetService.list_recent_tweets(user)
        if tweets_query:
            serializer = TweetSerializer(tweets_query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "no tweets found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"], url_path='get_users_tweets')
    def get_users_tweets(self, request):
        user = TwitterUserService.find_user_by_id(int(request.data.get('user_id'))).first()
        users_tweets = TweetService.find_users_tweets(request.data, user)
        if users_tweets:
            tweets = TweetSerializer(users_tweets, many=True)
            return Response(tweets.data, status=status.HTTP_200_OK)
        elif users_tweets == None: return Response({"error": "users selected dont have tweets asinged to them"}, status=status.HTTP_204_NO_CONTENT)
        else: return Response({"error": "users selected dont exist"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], url_path='like_tweet')
    def like_tweet(self, request, pk=None):
        user = TwitterUserService.find_user_by_id(int(request.data.get('user_id'))).first()
        updated_tweet = TweetService.like_tweet(pk, user)
        if updated_tweet:
            serializer = TweetSerializer(updated_tweet)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response({"error": "tweet selected dont exist"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], url_path='comment_tweet')
    def comment_tweet(self, request, pk=None):
        updated_tweet = TweetService.comment_tweet(pk, request)
        if updated_tweet:
            serializer = TweetSerializer(updated_tweet)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response({"error": "tweet selected dont exist"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"], url_path='get_tweet_comment')
    def comment_tweet(self, request, pk=None):
        result = TweetService.get_comments_by_id(pk)
        if result:
            comments = [
                {
                    "id": comment.id,
                    "text": comment.text,
                    "likes": comment.count
                } for comment in result
            ]
            return Response(comments, status=status.HTTP_200_OK)
        else: return Response({"error": "tweet selected dont exist"}, status=status.HTTP_400_BAD_REQUEST)

