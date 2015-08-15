from __future__ import absolute_import
from celery import shared_task
from .models import SocialSetting, Hashtag, Tweet, Verified, Team
import oauth2 as oauth
#from instagram.client import InstagramAPI
import json

def processTwitterHashtag(tweet,tweet_hashtags):
    if len(tweet_hashtags) > 0:
        hashtags = Hashtag.objects.all()
        for hashtag in hashtags:
            for tweet_hashtag in tweet_hashtags:
                if hashtag.hashtag.lower() == tweet_hashtag.get('text').lower():
                    hashtag.tweets.add(tweet)
                    hashtag.tweet_count += 1
                    if tweet.known_user:
                        hashtag.verified_count += 1
                    else:
                        hashtag.unverified_count += 1
                    hashtag.save()

def teamTwitter(tweet,member):
    teams = Team.objects.all()
    for team in teams:
        team_members = team.members.all()
        if len(team_members) > 0:
            for team_member in team_members:
                if team_member.display_name.lower() == member.display_name.lower():
                    team.tweets.add(tweet)
                    team.tweet_count += 1
                    team.save()

def saveVerifiedTwitter(tweet):
    ver = Verified.objects.all()
    for member in ver:
        if member.twitter_name.lower() == tweet.user_name.lower():
            member.tweets.add(tweet)
            member.tweet_count += 1
            member.save()
            teamTwitter(tweet,member)

def verifiedTwitter(tweet):
    ver = Verified.objects.all()
    known = False
    for member in ver:
        if member.twitter_name.lower() == tweet.user_name.lower():
            known = True
    return known

def processTweets(tweets):
    for tweet in tweets.get('statuses'):
        user_name = tweet.get('user').get('screen_name')
        check_exist = len(Tweet.objects.filter(content_id=int(tweet.get('id'))))
        if check_exist == 0:
            t = Tweet(user_name=user_name,content_id=int(tweet.get('id')))
            t.content = tweet.get('text')
            t.content_date = tweet.get('created_at')
            t.profile_pic = tweet.get('user').get('profile_image_url_https')
            t.content_type = "tweet"
            if tweet.get('coordinates'):
                if tweet.get('coordinates').get('type'):
                    if tweet.get('coordinates').get('type') == 'Point':
                        t.lat = tweet.get('geo').get('coordinates')[0]
                        t.lon = tweet.get('geo').get('coordinates')[1]
            t.save()
            t.known_user = verifiedTwitter(t)
            if t.known_user:
                saveVerifiedTwitter(t)
                t.save()
            processTwitterHashtag(t,tweet.get("entities").get("hashtags"))

@shared_task
def get_twitter():
    hashtags = ""
    divider = ""
    hashmark = "%23"
    hashtag = Hashtag.objects.all()
    if len(hashtag) > 0:
        for tag in hashtag:
            hashtags += divider + hashmark + tag.hashtag
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