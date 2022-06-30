from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from ..models import Tweet, TwitterUser
from .serializers import TweetSerializer, TwitterUserSerializer

class TwitterUserViewSet(viewsets.ModelViewSet):
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TwitterUser.create_user(serializer, request.data['password'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

      
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer