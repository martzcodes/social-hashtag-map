from rest_framework import serializers

from .models import Tweet, Insta, Team, Verified, Hashtag

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user_name', 'known_user', 'content', 'lat', 'lon', 'profile_pic', 'content_date')

class TeamStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('team_name', 'van_name', 'tweet_count', 'insta_count')

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