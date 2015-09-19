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
    instagram_hashtag = models.CharField(max_length=200, blank=True, null=True)
    def __unicode__(self):
        return self.api_name

class Post(models.Model):
    TWITTER = 'TW'
    INSTAGRAM = 'IN'
    RUNKEEPER = 'RK'
    SOURCE_CHOICES = (
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram'),
        (RUNKEEPER, 'Runkeeper'),
    )
    user_name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    known_user = models.BooleanField(default=False)
    source_type = models.CharField(max_length=2,
                                      choices=SOURCE_CHOICES,
                                      default=TWITTER)
    content = models.CharField(max_length=200, blank=True, null=True)
    content_id = models.CharField(max_length=200, unique=True)
    content_type = models.CharField(max_length=200, blank=True, null=True)
    thumbnail_link = models.CharField(max_length=200, blank=True, null=True)
    image_link = models.CharField(max_length=200, blank=True, null=True)
    has_location = models.BooleanField(default=False)
    lat = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
    lon = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.CharField(max_length=200, blank=True, null=True)
    content_date = models.CharField(max_length=200, blank=True, null=True)
    def __unicode__(self):
        return self.user_name

class Verified(models.Model):
    HOMEBASE = 'XX'
    TEAMONE = 'T1'
    TEAMTWO = 'T2'
    VANONE = 'V1'
    VANTWO = 'V2'
    TEAM_CHOICES = (
        (HOMEBASE, 'Home Base'),
        (TEAMONE, 'Team 1'),
        (TEAMTWO, 'Team 2'),
    )
    VAN_CHOICES = (
        (HOMEBASE, 'Home Base'),
        (VANONE, 'Van 1'),
        (VANTWO, 'Van 2'),
    )
    display_name = models.CharField(max_length=200, unique=True)
    twitter_name = models.CharField(max_length=200, blank=True, null=True)
    twitter_id = models.CharField(max_length=200, blank=True, null=True)
    instagram_name = models.CharField(max_length=200, blank=True, null=True)
    instagram_id = models.CharField(max_length=200, blank=True, null=True)
    runkeeper_name = models.CharField(max_length=200, blank=True, null=True)
    runkeeper_id = models.CharField(max_length=200, blank=True, null=True)
    team_choice = models.CharField(max_length=2,
                                      choices=TEAM_CHOICES,
                                      default=HOMEBASE)
    van_choice = models.CharField(max_length=2,
                                      choices=VAN_CHOICES,
                                      default=HOMEBASE)
    runner_number = models.IntegerField(default=0)
    posts = models.ManyToManyField(Post)
    tweet_count = models.IntegerField(default=0)
    insta_count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.display_name

class Hashtag(models.Model):
    hashtag = models.CharField(max_length=200)
    tweet_count = models.IntegerField(default=0)
    verified_count = models.IntegerField(default=0)
    unverified_count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.hashtag