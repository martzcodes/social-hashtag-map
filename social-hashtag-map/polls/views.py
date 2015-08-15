from rest_framework import generics, permissions
from .models import Tweet
from .serializers import TweetSerializer
from django.shortcuts import render


class TweetList(generics.ListCreateAPIView):
    model = Tweet
    serializer_class = TweetSerializer
    permission_classes = [
        permissions.AllowAny
    ]

def index(request):
    return render(request, 'polls/index.html')
