from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    #header_photo = models.ImageField()
    #profile_photo = ImageField()
    bio = models.TextField(max_length=160, default="hey I'm using Twitter", blank=True)
    location = models.CharField(max_length=100, default="no location of user registered", blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=14, blank=True)
    birth_date = models.DateField(blank=True)

    follows = models.ManyToManyField('self')

    followers = models.ManyToManyField('self')
    

    class Meta:
        ordering = ['id']
        verbose_name = 'twitter_user'
        verbose_name_plural = 'twitter_users'

    def __str__(self):
        return self.username


class Tweet(models.Model):
    text = models.CharField(max_length=280, blank=False)
    #midea = models.FileField(upload_to='uploads/')
    location = models.CharField(max_length=100, default="no location of tweet registered", blank=True)
    
    likes = models.ForeignKey(TwitterUser, related_name='tweet_likes', on_delete=models.CASCADE)
    
    retweets = models.ManyToManyField('self')

    class Meta:
        ordering = ['id']
        verbose_name = 'tweet'
        verbose_name_plural = 'tweets'

    def __str__(self):
        return self.text
