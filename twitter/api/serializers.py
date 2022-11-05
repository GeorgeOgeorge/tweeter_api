from rest_framework import serializers

from twitter.models import Tweet, TwitterUser
from twitter.service import TweetService, TwitterUserService


class TwitterUserSerializer(serializers.ModelSerializer):

    tweets = serializers.SerializerMethodField()
    follows = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = TwitterUser
        fields = [
            'id',
            'username',
            'password',
            'bio',
            'tweets',
            'follows',
            'followers',
            'email',
            'location',
            'website',
            'phone',
            'birth_date',
            'date_joined',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'tweets':{'read_only': True},
            'date_joined': {'read_only': True}
        }

    def get_tweets(self, obj):
        return [
            TweetSerializer(tweet).data
            for tweet in TweetService.find_tweets_by_user_id(obj.id)
        ]

    def get_follows(self, obj):
        follows = TwitterUserService.find_user_by_id(obj.id).get().follows.all()
        return [
            {
                "id": user.id,
                "name": user.username
            } for user in follows
        ]

    def get_followers(self, obj):
        followers = TwitterUserService.find_user_by_id(obj.id).get().followers.all()
        return [
            {
                "id": user.id,
                "name": user.username
            } for user in followers
        ]


class TweetSerializer(serializers.ModelSerializer):

    tweet_op = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    retweets = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'id',
            'text',
            'location',
            'tweet_op',
            'likes',
            'retweets'
        ]

    def get_tweet_op(self, obj):
        return {
            "id": obj.tweet_op.id,
            "username": obj.tweet_op.username
        }

    def get_likes(self, obj):
        return [
            {
                "id": user.id,
                "username": user.username
            } for user in obj.likes.all()
        ]

    def get_retweets(self, obj):
        return [
            {
                "id": comment.id,
                "text": comment.text,
                "likes": comment.likes.count(),
                "op_id": comment.tweet_op.id,
                "op_name": comment.tweet_op.username
            } for comment in obj.retweets.all()
        ]
