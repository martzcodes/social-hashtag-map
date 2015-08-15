from rest_framework import serializers

from .models import Tweet, Insta

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user_name', 'known_user', 'content', 'lat', 'lon', 'profile_pic', 'content_date')