from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('twitter_api/', include('twitter.api.urls'))
]
