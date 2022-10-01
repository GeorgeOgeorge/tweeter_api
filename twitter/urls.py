from django.urls import path

from twitter.views import teste


urlpatterns = [
    path('', teste, name='teste_render'),
]
