from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .models import Tweet, Team, Verified, Hashtag, Insta
from .serializers import TweetSerializer, HashtagStatSerializer, TeamStatSerializer, MemberStatSerializer
# from .serializers import StatSerializer
from django.shortcuts import render
import django_filters

class TweetList(generics.ListAPIView):
    #queryset = Tweet.objects.all()
    queryset = Tweet.objects.exclude(content__exact='')
    serializer_class = TweetSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class TeamStatsList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamStatSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class MemberStatsList(generics.ListAPIView):
    queryset = Verified.objects.all()
    serializer_class = MemberStatSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class HashtagStatsList(generics.ListAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagStatSerializer
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

# class AllStatsList(generics.ListAPIView):
#     serializer_class = StatsSerializer
#     def get_queryset(self):
#         return list(itertools.chain(Hashtag.objects.all(), Team.objects.all(), Member.objects.all()))

def index(request):
    return render(request, 'polls/index.html')
