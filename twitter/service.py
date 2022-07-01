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


class TweetService():
    
    def list_recent_tweets():
        return Tweet.objects.all().order_by('-created')[:10]
    
    
