from django.contrib import admin
from polls.models import SocialSetting, Hashtag, Verified, Post

admin.site.register(SocialSetting)
admin.site.register(Hashtag)
admin.site.register(Verified)
admin.site.register(Post)