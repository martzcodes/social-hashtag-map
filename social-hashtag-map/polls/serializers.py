from rest_framework import serializers

from .models import Post, Verified, Hashtag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user_name', 'known_user', 'content', 'lat', 'lon', 'profile_pic', 'content_date')

class MemberStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verified
        fields = ('display_name', 'tweet_count', 'insta_count')

class HashtagStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('hashtag', 'tweet_count', 'insta_count', 'verified_count', 'unverified_count')

# class StatSerializer(serializers.Serializer):
#     pk = serializers.Field()
#     title = serializers.CharField()
#     author = serializers.RelatedField()
#     pub_date = serializers.DateTimeField()