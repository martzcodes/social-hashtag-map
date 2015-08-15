from rest_framework import serializers

from .models import Tweet, Insta

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user_name', 'known_user', 'content', 'lat', 'lon', 'profile_pic', 'content_date')

# class Tweet(models.Model):
#     user_name = models.CharField(max_length=200)
#     known_user = models.BooleanField(default=False)
#     content = models.CharField(max_length=200, blank=True, null=True)
#     content_id = models.CharField(max_length=200, unique=True)
#     content_type = models.CharField(max_length=200, blank=True, null=True)
#     lat = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
#     lon = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
#     link = models.CharField(max_length=200, blank=True, null=True)
#     profile_pic = models.CharField(max_length=200, blank=True, null=True)
#     content_date = models.CharField(max_length=200, blank=True, null=True)
#     def __unicode__(self):
#         return self.user_name