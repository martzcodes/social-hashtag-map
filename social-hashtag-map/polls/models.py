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
    api_client_id = models.CharField(max_length=200)
    api_client_secret = models.CharField(max_length=200)
    api_access_token = models.CharField(max_length=200)
    api_last_id = models.CharField(max_length=200)

class Hashtag(models.Model):
    settings = models.ForeignKey(SocialSetting)
    user = models.CharField(max_length=200)
    tweet_count = models.IntegerField(default=0)
    insta_count = models.IntegerField(default=0)
    verified_count = models.IntegerField(default=0)
    unverified_count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.hashtag

class Verified(models.Model):
    display_name = models.CharField(max_length=200)
    twitter_name = models.CharField(max_length=200)
    twitter_id = models.CharField(max_length=200)
    instagram_name = models.CharField(max_length=200)
    instagram_id = models.CharField(max_length=200)
    runkeeper_name = models.CharField(max_length=200)
    runkeeper_id = models.CharField(max_length=200)
    tweet_count = models.IntegerField(default=0)
    insta_count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.display_name

class Team(models.Model):
    members = models.ForeignKey(Verified)
    team_name = models.CharField(max_length=200)
    van_name = models.CharField(max_length=200)
    tweet_count = models.IntegerField(default=0)
    insta_count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.team_name + self.van_name

class Tweet(models.Model):
    hashtag = models.ForeignKey(Hashtag)
    user_name = models.CharField(max_length=200)
    verified = models.ForeignKey(Verified)
    content = models.CharField(max_length=200)
    content_id = models.CharField(max_length=200)
    content_type = models.CharField(max_length=200)
    lat = models.DecimalField(decimal_places=17,max_digits=20)
    lon = models.DecimalField(decimal_places=17,max_digits=20)
    link = models.CharField(max_length=200)
    profile_pic = models.CharField(max_length=200)
    content_date = models.CharField(max_length=200)
    def __unicode__(self):
        return self.user_name + self.content

class Insta(models.Model):
    hashtag = models.ForeignKey(Hashtag)
    user_name = models.CharField(max_length=200)
    verified = models.ForeignKey(Verified)
    content = models.CharField(max_length=200)
    caption_text = models.CharField(max_length=200)
    content_type = models.CharField(max_length=200)
    thumbnail_link = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200)
    lat = models.DecimalField(decimal_places=17,max_digits=20)
    lon = models.DecimalField(decimal_places=17,max_digits=20)
    link = models.CharField(max_length=200)
    content_date = models.CharField(max_length=200)
    def __unicode__(self):
        return self.user_name + self.caption_text