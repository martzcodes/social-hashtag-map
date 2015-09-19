from __future__ import absolute_import
from celery import shared_task
from .models import SocialSetting, Hashtag, Post, Verified
import oauth2 as oauth
from instagram.client import InstagramAPI
import json

def processTwitterHashtag(tweet,tweet_hashtags):
    if len(tweet_hashtags) > 0:
        hashtags = Hashtag.objects.all()
        for hashtag in hashtags:
            for tweet_hashtag in tweet_hashtags:
                if hashtag.hashtag.lower() == tweet_hashtag.get('text').lower():
                    hashtag.tweet_count += 1
                    if tweet.known_user:
                        hashtag.verified_count += 1
                    else:
                        hashtag.unverified_count += 1
                    hashtag.save()

def saveVerifiedTwitter(tweet):
    ver = Verified.objects.all()
    for member in ver:
        if member.twitter_name.lower() == tweet.user_name.lower():
            member.posts.add(tweet)
            member.tweet_count += 1
            member.save()
            tweet.display_name = member.display_name
            tweet.save()

def verifiedTwitter(tweet):
    ver = Verified.objects.all()
    known = False
    for member in ver:
        if member.twitter_name.lower() == tweet.user_name.lower():
            known = True
    return known

def processTweets(tweets):
    for tweet in reversed(tweets.get('statuses')): #reversed because twitter gives them in the order of most recent first
        user_name = tweet.get('user').get('screen_name')
        check_exist = len(Post.objects.filter(content_id=int(tweet.get('id'))))
        if check_exist == 0:
            t = Post(user_name=user_name,content_id=int(tweet.get('id')),source_type='TW')
            t.content = tweet.get('text')
            t.content_date = tweet.get('created_at')
            t.profile_pic = tweet.get('user').get('profile_image_url')
            t.content_type = "tweet"
            if tweet.get('coordinates'):
                if tweet.get('coordinates').get('type'):
                    if tweet.get('coordinates').get('type') == 'Point':
                        t.has_location = True
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
            divider = "+OR+"
    else:
        hashtags = "%23freeragnarbeer" #note: %23 is the url encoding of '#'
    api = SocialSetting.objects.filter(api_type='TW')[0]
    if api:
        key = api.api_client_id
        secret = api.api_client_secret
        consumer = oauth.Consumer(key, secret)
        client = oauth.Client(consumer)
        if api.api_last_id:
            resp, content = client.request('https://api.twitter.com/1.1/search/tweets.json' + 
                                            '?q='+hashtags+'&result_type=recent'+
                                            '&since_id='+api.api_last_id, "GET")
        else:
            resp, content = client.request('https://api.twitter.com/1.1/search/tweets.json' + 
                                            '?q='+hashtags+'&result_type=recent',
                                            "GET")
        freeragnarbeer = json.loads(content)
        if "statuses" in freeragnarbeer:
            if len(freeragnarbeer["statuses"]) > 0:
                api.api_last_id = str(freeragnarbeer["statuses"][0]["id"])
                api.save()
                processTweets(freeragnarbeer)
                return "Success, processing tweets"
            else:
                return "Success, but no tweets"
        else:
            return "Success, but no tweets"
    else:
        return "No Twitter API"

def saveVerifiedInstagram(insta):
    ver = Verified.objects.all()
    for member in ver:
        if member.instagram_name.lower() == insta.user_name.lower():
            member.posts.add(insta)
            member.insta_count += 1
            member.save()
            insta.display_name = member.display_name
            insta.save()

def verifiedInstagram(insta):
    ver = Verified.objects.all()
    known = False
    for member in ver:
        if member.instagram_name.lower() == insta.user_name.lower():
            known = True
    return known

def processInstas(instas):
    for insta in reversed(instas):
        user_name = insta.user.username
        # print insta.caption.text
        # for property, value in vars(insta.images.get('thumbnail')).iteritems():
        #     print property, ": ", value
        # print insta.images.get('thumbnail').url
        check_exist = len(Post.objects.filter(content_id=insta.id))
        if check_exist == 0:
            i = Post(user_name=user_name,content_id=insta.id,source_type='IN')

            i.content = insta.caption.text
            i.content_date = insta.created_time
            i.profile_pic = insta.user.profile_picture
            i.content_type = "insta"
            i.thumbnail_link = insta.images.get('thumbnail').url
            i.image_link = insta.images.get('standard_resolution').url
            i.save()
            i.known_user = verifiedInstagram(i)
            if i.known_user:
                saveVerifiedInstagram(i)
                i.save()

@shared_task
def get_instagram():
    api = SocialSetting.objects.filter(api_type='IN')[0]
    secret = api.api_client_secret
    token = api.api_access_token
    req = InstagramAPI(access_token=token, client_secret=secret)
    if api:
        if api.api_last_id:
            recent_tags, next_ = req.tag_recent_media(tag_name=api.instagram_hashtag, count=10, max_tag_id=api.api_last_id) #accepts_parameters=['count', 'max_tag_id', 'tag_name'],
        else:
            recent_tags, next_ = req.tag_recent_media(tag_name=api.instagram_hashtag, count=10) #accepts_parameters=['count', 'max_tag_id', 'tag_name'],
        #recent_tags, next_ = api.tag_recent_media(tag_name="tgif", count=10, max_tag_id="1051706417356389558_318480430") #accepts_parameters=['count', 'max_tag_id', 'tag_name'],
        if len(recent_tags) > 0:
            api.api_last_id = recent_tags[0].id
            api.save()
            processInstas(recent_tags)
            return "Success, processing"
        else:
            return "Nothing to process"
    else:
        return "No Instgram API"

@shared_task
def get_social():
    get_twitter()
    get_instagram()
    return "Requested"