from __future__ import absolute_import
from django.db import IntegrityError
from celery import shared_task
from .models import SocialSetting, Hashtag, Tweet, Verified
import oauth2 as oauth
#from instagram.client import InstagramAPI
import json

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

def knownTwitter(user_name):
    ver = Verified.objects.all()
    known = False
    for member in ver:
        if member.twitter_name == user_name:
            known = True
    return known

def processTweets(tweets):
    for tweet in tweets.get('statuses'):
        user_name = tweet.get('user').get('screen_name')
        t = Tweet(user_name=user_name,content_id=int(tweet.get('id')))
        t.content = tweet.get('text')
        t.known_user=knownTwitter(user_name)
        t.content_date = tweet.get('created_at')
        t.profile_pic = tweet.get('user').get('profile_image_url_https')
        t.content_type = "tweet"
        if tweet.get('coordinates'):
            if tweet.get('coordinates').get('type'):
                if tweet.get('coordinates').get('type') == 'Point':
                    t.lat = tweet.get('geo').get('coordinates')[0]
                    t.lon = tweet.get('geo').get('coordinates')[1]
        try:
            t.save()
        except IntegrityError as e:
            print "Tweet Id already exists"

@shared_task
def get_twitter():
    hashtags = ""
    divider = ""
    hashtag = Hashtag.objects.all()
    if len(hashtag) > 0:
        for tag in hashtag:
            hashtags += divider + tag
            divider = "&"
    else:
        hashtags = "%23freeragnarbeer" #note: %23 is the url encoding of '#'
    api = SocialSetting.objects.filter(api_type='TW')
    if api[0]:
        key = api[0].api_client_id
        secret = api[0].api_client_secret
        consumer = oauth.Consumer(key, secret)
        client = oauth.Client(consumer)
        if api[0].api_last_id:
            resp, content = client.request('https://api.twitter.com/1.1/search/tweets.json' + 
                                            '?q='+hashtags+'&result_type=recent'+
                                            '&since_id='+api[0].api_last_id, "GET")
        else:
            resp, content = client.request('https://api.twitter.com/1.1/search/tweets.json' + 
                                            '?q='+hashtags+'&result_type=recent',
                                            "GET")
        freeragnarbeer = json.loads(content)
        processTweets(freeragnarbeer)
        return "Success"
    else:
        return "No Apis"


@shared_task
def get_instagram():
    api = SocialSetting.objects.filter(api_type='IN')
    return api[0].api_name