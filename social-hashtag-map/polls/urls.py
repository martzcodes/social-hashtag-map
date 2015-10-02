from django.conf.urls import patterns, url, include

from .views import PostList, PostListTweet, PostListInsta, PostListRecent, PostListLocation, MemberStatsList, HashtagStatsList


urlpatterns = patterns('polls.views',
    url(r'^posts$', PostList.as_view(), name='posts_list'),
    url(r'^posts/recent$', PostListRecent.as_view(), name='posts_list'),
    url(r'^posts/tweets$', PostListTweet.as_view(), name='posts_list'),
    url(r'^posts/instas$', PostListInsta.as_view(), name='posts_list'),
    url(r'^posts/location$', PostListLocation.as_view(), name='posts_list'),
    url(r'^member/stats$', MemberStatsList.as_view(), name='posts_list'),
    url(r'^hashtag/stats$', HashtagStatsList.as_view(), name='posts_list'),
    # url(r'^posts/(?P<question_pk>[0-9]+)/$', QuestionDetail.as_view(), 
    #       name="questions_detail"),
    # url(r'^choices$', ChoiceList.as_view(), name='choices_list'),
    # url(r'^choices/(?P<choice_pk>[0-9]+)/$', ChoiceUpdate.as_view(), 
    #       name='choices_update'),
    url(r'^$', 'index', name='posts_index'),
)
