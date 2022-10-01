from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('twitter.urls')),
    path('twitter_api/', include('twitter.api.urls')),
    path('admin/', admin.site.urls)
]
