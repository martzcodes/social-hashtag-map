from django.conf.urls import patterns, url, include

from .views import TweetList #, ChoiceList, QuestionDetail, ChoiceUpdate


urlpatterns = patterns('polls.views',
	url(r'^tweets$', TweetList.as_view(), name='tweets_list'),
	# url(r'^tweets/(?P<question_pk>[0-9]+)/$', QuestionDetail.as_view(), 
	# 		name="questions_detail"),
	# url(r'^choices$', ChoiceList.as_view(), name='choices_list'),
	# url(r'^choices/(?P<choice_pk>[0-9]+)/$', ChoiceUpdate.as_view(), 
	# 		name='choices_update'),
	url(r'^$', 'index', name='tweets_index'),
)
