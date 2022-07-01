from .models import TwitterUser, Tweet


class TwitterUserService():

    def create_user(serializer, user_pass):
        new_user = TwitterUser(
            username = serializer.data['username'],
            bio = serializer.data['bio'],
            email = serializer.data['email'],
            location = serializer.data['location'],
            website = serializer.data['website'],
            phone = serializer.data['phone'],
            birth_date = serializer.data['birth_date'],
            is_superuser = True
        )
        new_user.set_password(user_pass)
        new_user.save()

    def find_user_by_id(id):
        result = TwitterUser.objects.filter(pk=id)
        return check_result_value(result)
        
    def find_user_by_username(name):
        result = TwitterUser.objects.filter(username__in=name)
        return check_result_value(result)


class TweetService():

    def create_tweet(serializer, tweet_op):
        tweet_op_result = TwitterUserService.find_user_by_id(tweet_op)
        if tweet_op_result != None:
            new_tweet = Tweet(
                text = serializer.data['text'],
                location = serializer.data['location'],
                tweet_op = tweet_op_result.get()
            )
            new_tweet.save()
            return True
        else: return False

    def list_recent_tweets():
        return Tweet.objects.all().order_by('-created')[:10]

    def find_tweets_by_user_id(user_id):
        result = Tweet.objects.filter(tweet_op=user_id)
        return check_result_value(result)

    def find_users_tweets(request):
        user_result = TwitterUserService.find_user_by_username(request['users'])
        if user_result != None:
            user_tweets = []
            for user in user_result:
                tweet_result = TweetService.find_tweets_by_user_id(user.id)
                if tweet_result != None:
                    for tweet in tweet_result: user_tweets.append(tweet) 
            return user_tweets
        else: return False


def check_result_value(result):
    if len(result) != 0: 
        return result
    else: 
        return None