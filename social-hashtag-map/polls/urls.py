from django.conf.urls import patterns, url, include

from .views import TweetList, VerifiedTweetList, UnVerifiedTweetList, LocationTweetList
from .views import MemberStatsList, TeamStatsList, HashtagStatsList


urlpatterns = patterns('polls.views',
    url(r'^tweets$', TweetList.as_view(), name='tweets_list'),
    url(r'^tweets/verified$', VerifiedTweetList.as_view(), name='tweets_list'),
    url(r'^tweets/unverified$', UnVerifiedTweetList.as_view(), name='tweets_list'),
    url(r'^tweets/location$', LocationTweetList.as_view(), name='tweets_list'),
    url(r'^member/stats$', MemberStatsList.as_view(), name='tweets_list'),
    url(r'^team/stats$', TeamStatsList.as_view(), name='tweets_list'),
    url(r'^hashtag/stats$', HashtagStatsList.as_view(), name='tweets_list'),
    # url(r'^tweets/(?P<question_pk>[0-9]+)/$', QuestionDetail.as_view(), 
    #       name="questions_detail"),
    # url(r'^choices$', ChoiceList.as_view(), name='choices_list'),
    # url(r'^choices/(?P<choice_pk>[0-9]+)/$', ChoiceUpdate.as_view(), 
    #       name='choices_update'),
    url(r'^$', 'index', name='tweets_index'),
)
