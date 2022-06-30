from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views import TwitterUserViewSet, TweetViewSet

router = DefaultRouter()
router.register(r'twitterusers', TwitterUserViewSet, basename='twitterusers')
router.register(r'tweets', TweetViewSet, basename='tweets')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh_token', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls