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

    @action(detail=False, methods=['POST'])
    def follow_user(self, request):
        user = TwitterUserService.follow_user(request.data.get("user_pk"), request.data.get("follow_pk"))
        if user:
            return Response(TwitterUserSerializer(user).data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "erro during follow process"}, status=status.HTTP_400_BAD_REQUEST)


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

    @action(detail=True, methods=["post"], url_path='comment_tweets')
    def comment_tweet(self, request, pk=None):
        updated_tweet = TweetService.comment_tweet(pk, request)
        if updated_tweet:
            serializer = TweetSerializer(updated_tweet)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response({"error": "tweet selected dont exist"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"])
    def get_tweet_comments(self, request, pk=None):
        pass

    @action(detail=True, methods=["get"])
    def tweet_replies(self, request, pk=None):
        tweet = TweetService.find_tweet_by_id(pk).get()
        if tweet:
            return Response(TweetSerializer(tweet).data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "tweet has no replies"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"])
    def get_user_tweets(self, request, pk):
        tweets = TweetService.find_tweets_by_user_id(pk)
        if tweets:
            return Response([TweetSerializer(tweet).data for tweet in tweets], status=status.HTTP_200_OK)
        else:
            return Response({"error": "user has no tweets"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"])
    def user_home(self, request, pk):
        tweets = TweetService.get_home_tweets(pk)
        if tweets:
            return Response([TweetSerializer(tweet).data for tweet in tweets], status=status.HTTP_200_OK)
        else:
            return Response({"error": "erro while getting tweets"}, status=status.HTTP_400_BAD_REQUEST)
