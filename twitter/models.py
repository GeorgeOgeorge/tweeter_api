from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    #header_photo = models.ImageField()
    #profile_photo = ImageField()
    bio = models.TextField(max_length=160, default="hey I'm using Twitter", blank=True, null=True)
    location = models.CharField(max_length=100, default="no location of user registered", blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    follows = models.ManyToManyField('self')
    followers = models.ManyToManyField('self')
    
    class Meta:
        ordering = ['id']
        verbose_name = 'twitter_user'
        verbose_name_plural = 'twitter_users'

    def __str__(self):
        return self.username

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


class Tweet(models.Model):
    text = models.CharField(max_length=280, blank=False)
    #midea = models.FileField(upload_to='uploads/')
    location = models.CharField(max_length=100, default="no location of tweet registered", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    tweet_op = models.ForeignKey(TwitterUser, related_name='tweet_op', on_delete=models.CASCADE)

    likes = models.ManyToManyField(TwitterUser, related_name='tweet_likes', blank=True)
    
    retweets = models.ManyToManyField('self', blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'tweet'
        verbose_name_plural = 'tweets'

    def __str__(self):
        return self.text
