from django.contrib import admin

from .models import TwitterUser, Tweet


admin.site.register(TwitterUser)
admin.site.register(Tweet)
