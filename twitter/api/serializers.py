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

    class Meta:
        model = TwitterUser
        fields = [
            'id',
            'username',
            'password',
            'email',
            'bio',
            'location',
            'website',
            'phone',
            'birth_date',
            'date_joined',
            'follows',
            'followers'
        ]

    def get_follows(self, obj):
        pass

    def get_followers(self, ojb):
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