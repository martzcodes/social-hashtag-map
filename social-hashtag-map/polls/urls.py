from django.conf.urls import patterns, url, include

from .views import PostList, VerifiedPostList, UnVerifiedPostList, LocationPostList
from .views import MemberStatsList, HashtagStatsList


urlpatterns = patterns('polls.views',
    url(r'^posts$', PostList.as_view(), name='posts_list'),
    url(r'^posts/verified$', VerifiedPostList.as_view(), name='posts_list'),
    url(r'^posts/unverified$', UnVerifiedPostList.as_view(), name='posts_list'),
    url(r'^posts/location$', LocationPostList.as_view(), name='posts_list'),
    url(r'^member/stats$', MemberStatsList.as_view(), name='posts_list'),
    url(r'^hashtag/stats$', HashtagStatsList.as_view(), name='posts_list'),
    # url(r'^posts/(?P<question_pk>[0-9]+)/$', QuestionDetail.as_view(), 
    #       name="questions_detail"),
    # url(r'^choices$', ChoiceList.as_view(), name='choices_list'),
    # url(r'^choices/(?P<choice_pk>[0-9]+)/$', ChoiceUpdate.as_view(), 
    #       name='choices_update'),
    url(r'^$', 'index', name='posts_index'),
)
