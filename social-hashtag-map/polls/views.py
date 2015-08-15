from rest_framework import generics, permissions, filters
from .models import Tweet
from .serializers import TweetSerializer
from django.shortcuts import render
import django_filters

class TweetList(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class VerifiedTweetList(generics.ListAPIView):
    queryset = Tweet.objects.filter(known_user=True)
    serializer_class = TweetSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UnVerifiedTweetList(generics.ListAPIView):
    queryset = Tweet.objects.filter(known_user=False)
    serializer_class = TweetSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LocationTweetList(generics.ListAPIView):
    queryset = Tweet.objects.filter(lat__isnull=False,lon__isnull=False)
    serializer_class = TweetSerializer
    permission_classes = [
        permissions.AllowAny
    ]

def index(request):
    return render(request, 'polls/index.html')
