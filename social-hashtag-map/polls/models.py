import datetime

from django.db import models
from django.utils import timezone


class SocialSetting(models.Model):
    TWITTER = 'TW'
    INSTAGRAM = 'IN'
    API_CHOICES = (
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram'),
    )
    api_type = models.CharField(max_length=2,
                                      choices=API_CHOICES,
                                      default=TWITTER)
    api_name = models.CharField(max_length=200)
    api_client_id = models.CharField(max_length=200, blank=True, null=True)
    api_client_secret = models.CharField(max_length=200)
    api_access_token = models.CharField(max_length=200, blank=True, null=True)
    api_last_id = models.CharField(max_length=200, blank=True, null=True)
    def __unicode__(self):
        return self.api_name

class Tweet(models.Model):
    user_name = models.CharField(max_length=200)
    known_user = models.BooleanField(default=False)
    content = models.CharField(max_length=200, blank=True, null=True)
    content_id = models.CharField(max_length=200, unique=True)
    content_type = models.CharField(max_length=200, blank=True, null=True)
    lat = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
    lon = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.CharField(max_length=200, blank=True, null=True)
    content_date = models.CharField(max_length=200, blank=True, null=True)
    def __unicode__(self):
        return self.user_name

class Insta(models.Model):
    user_name = models.CharField(max_length=200)
    known_user = models.BooleanField(default=False)
    caption_text = models.CharField(max_length=200, blank=True, null=True)
    content_type = models.CharField(max_length=200, blank=True, null=True)
    thumbnail_link = models.CharField(max_length=200, blank=True, null=True)
    image_link = models.CharField(max_length=200, blank=True, null=True)
    lat = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
    lon = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    content_date = models.CharField(max_length=200, blank=True, null=True)
    def __unicode__(self):
        return self.user_name

class Verified(models.Model):
    display_name = models.CharField(max_length=200)
    twitter_name = models.CharField(max_length=200, blank=True, null=True)
    twitter_id = models.CharField(max_length=200, blank=True, null=True)
    instagram_name = models.CharField(max_length=200, blank=True, null=True)
    instagram_id = models.CharField(max_length=200, blank=True, null=True)
    runkeeper_name = models.CharField(max_length=200, blank=True, null=True)
    runkeeper_id = models.CharField(max_length=200, blank=True, null=True)
    tweets = models.ForeignKey(Tweet, blank=True, null=True)
    instas = models.ForeignKey(Insta, blank=True, null=True)
    tweet_count = models.IntegerField(default=0)
    insta_count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.display_name

class Team(models.Model):
    members = models.ForeignKey(Verified, blank=True, null=True)
    team_name = models.CharField(max_length=200)
    van_name = models.CharField(max_length=200, blank=True, null=True)
    tweet_count = models.IntegerField(default=0)
    insta_count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.team_name

class Hashtag(models.Model):
    hashtag = models.CharField(max_length=200)
    tweets = models.ForeignKey(Tweet, blank=True, null=True)
    instas = models.ForeignKey(Insta, blank=True, null=True)
    tweet_count = models.IntegerField(default=0)
    insta_count = models.IntegerField(default=0)
    verified_count = models.IntegerField(default=0)
    unverified_count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.hashtag