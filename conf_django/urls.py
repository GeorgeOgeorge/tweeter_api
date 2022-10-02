from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('twitter_api/', include('twitter.api.urls')),
    path('admin/', admin.site.urls)
]
