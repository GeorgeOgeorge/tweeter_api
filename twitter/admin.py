from django.contrib import admin

from twitter.models import Tweet, TwitterUser

admin.site.register(TwitterUser)
admin.site.register(Tweet)
