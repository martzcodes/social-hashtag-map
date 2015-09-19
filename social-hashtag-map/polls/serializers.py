from rest_framework import serializers

from .models import Post, Verified, Hashtag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user_name', 'known_user', 'content', 'lat', 'lon', 'profile_pic', 'content_date', 'source_type', 'has_location', 'thumbnail_link', 'image_link', 'display_name')

class MemberStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verified
        fields = ('display_name', 'tweet_count', 'insta_count', 'team_choice', 'van_choice', 'runner_number')

class HashtagStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('hashtag', 'verified_count', 'unverified_count')

# class StatSerializer(serializers.Serializer):
#     pk = serializers.Field()
#     title = serializers.CharField()
#     author = serializers.RelatedField()
#     pub_date = serializers.DateTimeField()