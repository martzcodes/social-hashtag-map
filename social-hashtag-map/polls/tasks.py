from __future__ import absolute_import

from celery import shared_task
from .models import SocialSetting, Hashtag
import oauth2 as oauth
#from instagram.client import InstagramAPI
import json


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
        return freeragnarbeer
    else:
        return "No Apis"


@shared_task
def get_instagram():
    api = SocialSetting.objects.filter(api_type='IN')
    return api[0].api_name