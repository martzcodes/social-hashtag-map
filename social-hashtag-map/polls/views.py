from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .models import Verified, Hashtag, Post
from .serializers import PostSerializer, HashtagStatSerializer, MemberStatSerializer
# from .serializers import StatSerializer
from django.shortcuts import render
import django_filters

class PostList(generics.ListAPIView):
    #queryset = Post.objects.all()
    queryset = Post.objects.exclude(content__exact='')
    serializer_class = PostSerializer
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

class VerifiedPostList(generics.ListAPIView):
    queryset = Post.objects.filter(known_user=True)
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UnVerifiedPostList(generics.ListAPIView):
    queryset = Post.objects.filter(known_user=False)
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LocationPostList(generics.ListAPIView):
    queryset = Post.objects.filter(lat__isnull=False,lon__isnull=False)
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

# class AllStatsList(generics.ListAPIView):
#     serializer_class = StatsSerializer
#     def get_queryset(self):
#         return list(itertools.chain(Hashtag.objects.all(), Team.objects.all(), Member.objects.all()))

def index(request):
    return render(request, 'polls/index.html')
