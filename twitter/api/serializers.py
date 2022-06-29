from rest_framework import serializers

from ..models import TwitterUser, Tweet

class TwitterUserSerializerLogin(serializers.ModelSerializer):
    
    class Meta:
        model = TwitterUser
        fiedls = [
            'username',
            'password'
        ]

class TwitterUserSerializer(serializers.ModelSerializer):
    
    follows = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    tweets = serializers.SerializerMethodField()

    class Meta:
        model = TwitterUser
        fields = [
            'id',
            'username',
            'password',
            'bio',
            'follows',
            'followers',
            'tweets',
            'email',
            'location',
            'website',
            'phone',
            'birth_date',
            'date_joined',
            'is_superuser'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'follows': {'read_only': True},
            'followers':{'read_only': True},
            'tweets':{'read_only': True},
            'is_superuser':{'write_only': True},
            'date_joined': {'read_only': True}
        }

    def get_follows(self, obj):
        pass

    def get_followers(self, obj):
        pass

    def get_tweets(self, obj):
        pass
    

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
        pass

    def get_likes(self, obj):
        pass

    def get_retweets(self, obj):
        pass