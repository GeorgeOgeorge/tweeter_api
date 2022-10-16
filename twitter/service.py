from django.contrib.auth import authenticate

from twitter.models import Tweet, TwitterUser


class TwitterUserService():

    def create_user(request):
        new_user = TwitterUser(
            username = request.data['username'],
            bio = request.data['bio'],
            email = request.data['email'],
            location = request.data['location'],
            website = request.data['website'],
            phone = request.data['phone'],
            birth_date = request.data['birth_date'],
            is_superuser = True
        )
        new_user.set_password(request.data['password'])
        new_user.save()
        return new_user

    def find_user_by_id(id):
        result = TwitterUser.objects.filter(pk=id)
        return check_result_value(result)

    def find_user_by_username(name, user):
        result = TwitterUser.objects.filter(username__in=name).exclude(id=user.id)
        return check_result_value(result)

    def login(request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        return user.id if user else None


class TweetService():

    def create_tweet(request, user):
        # breakpoint()
        new_tweet = Tweet(
            text = request.data['text'],
            location = request.data['location'],
            tweet_op = user
        )
        new_tweet.save()
        return new_tweet

    def like_tweet(tweet_id, user):
        tweet_result = TweetService.find_tweet_by_id(tweet_id)
        if tweet_result:
            tweet = tweet_result.get()
            tweet.likes.add(user)
            tweet.save()
            return tweet
        else: return None

    def comment_tweet(tweet_id, request):
        tweet_result = TweetService.find_tweet_by_id(tweet_id)
        if tweet_result:
            comment = TweetService.create_tweet(request, request.user)
            tweet = tweet_result.get()
            tweet.retweets.add(comment)
            tweet.save()
            return tweet
        else: return None

    def list_recent_tweets(user):
        return Tweet.objects.all().order_by('-created').exclude(tweet_op=user.id)[:10]

    def find_tweet_by_id(tweet_id):
        result = Tweet.objects.filter(pk=tweet_id)
        return check_result_value(result)

    def find_tweets_by_user_id(user_id):
        result = Tweet.objects.filter(tweet_op=user_id)
        return check_result_value(result)

    def find_users_tweets(request, user):
        user_result = TwitterUserService.find_user_by_username(request['users'], user)
        if user_result != None:
            user_tweets = []
            for user in user_result:
                tweet_result = TweetService.find_tweets_by_user_id(user.id)
                if tweet_result != None:
                    for tweet in tweet_result: user_tweets.append(tweet) 
            return user_tweets
        else: return False

    def find_tweet_likes_by_id(tweet_id):
        tweets_likes = []
        likes_result = TwitterUser.objects.filter(tweet_likes__id=tweet_id)
        for likes in likes_result:
            tweets_likes.append(likes)
        return tweets_likes

    def find_tweet_retweets_by_id(tweet_id):
        tweet_retweets = []
        retweets_result = Tweet.objects.filter(retweets__id=tweet_id)
        for retweets in retweets_result:
            tweet_retweets.append(retweets)
        return tweet_retweets

def check_result_value(result):
    if len(result) != 0: 
        return result
    else: 
        return None