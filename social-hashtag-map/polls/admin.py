from django.contrib import admin
from polls.models import SocialSetting, Hashtag, Verified, Team, Tweet, Insta

admin.site.register(SocialSetting)
admin.site.register(Hashtag)
admin.site.register(Verified)
admin.site.register(Team)
admin.site.register(Tweet)
admin.site.register(Insta)