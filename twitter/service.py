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

    def username_exists(name):
        return TwitterUser.objects.filter(username=name).exists()

    def login(request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        return user.id if user else None

    def follow_user(user_pk, follow_pk):
        user = TwitterUserService.find_user_by_id(user_pk).first()
        target = TwitterUserService.find_user_by_id(follow_pk).first()

        if user and target:
            if not user.follows.contains(target) and not target.followers.contains(user):
                user.follows.add(target)
                target.followers.add(user)
            else:
                user.follows.remove(target)
                target.followers.remove(user)
            user.save()
            target.save()
            return user
        return None


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

            if tweet.likes.contains(user):
                tweet.likes.remove(user)
            else:
                tweet.likes.add(user)
                tweet.save()
            return tweet
        else: return None

    def comment_tweet(tweet_id, request):
        tweet_result = TweetService.find_tweet_by_id(tweet_id)
        if tweet_result:
            user = TwitterUserService.find_user_by_id(int(request.data.get('user_id')))
            comment = TweetService.create_tweet(request, user.first())
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

    def get_comments_by_id(tweet_id):
        breakpoint()
        x = Tweet.objects.filter(pk=tweet_id).get()
        return [
            {
                "id": comment.id,
                "text": comment.text,
                "likes": comment.likes.count(),
                "op_id": comment.tweet_op.id,
                "op_name": comment.tweet_op.name
            } for comment in x.retweets
        ]

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

    def get_home_tweets(user_id):
        user = TwitterUserService.find_user_by_id(user_id).get()
        breakpoint()
        if user.follows.exists():
            return [
                {
                    "id": tweet.id,
                    "text": tweet.text,
                    "tweet_op": tweet.tweet_op.username,
                    "comments": [
                        {
                            "id": comment.id,
                            "text": comment.text,
                            "likes": comment.count
                        } for comment in TweetService.get_comments_by_id(tweet.id)
                    ]
                }
                for tweet in [TweetService.find_tweets_by_user_id(follow.id) for follow in user.follows]
            ]
        return Tweet.objects.all().order_by('-created')


def check_result_value(result):
    if len(result) != 0:
        return result
    else:
        return None