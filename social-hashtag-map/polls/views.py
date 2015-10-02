from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .models import Verified, Hashtag, Post
from .serializers import PostSerializer, HashtagStatSerializer, MemberStatSerializer
# from .serializers import StatSerializer
from django.shortcuts import render
import django_filters

class PostList(generics.ListAPIView):
    #queryset = Post.objects.all()
    queryset = Post.objects.exclude(content__exact='').order_by('id')
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PostListRecent(generics.ListAPIView):
    #queryset = Post.objects.all()
    queryset = Post.objects.exclude(content__exact='').order_by('-id')[:10]
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PostListTweet(generics.ListAPIView):
    #queryset = Post.objects.all()
    queryset = Post.objects.exclude(content__exact='').filter(api_type='TW').order_by('-id')[:10]
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PostListInsta(generics.ListAPIView):
    #queryset = Post.objects.all()
    queryset = Post.objects.exclude(content__exact='').filter(api_type='IN').order_by('-id')[:10]
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PostListLocation(generics.ListAPIView):
    #queryset = Post.objects.all()
    queryset = Post.objects.exclude(content__exact='').filter(known_user=True).filter(has_location=True)
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

# class AllStatsList(generics.ListAPIView):
#     serializer_class = StatsSerializer
#     def get_queryset(self):
#         return list(itertools.chain(Hashtag.objects.all(), Team.objects.all(), Member.objects.all()))

def index(request):
    return render(request, 'polls/index.html')
