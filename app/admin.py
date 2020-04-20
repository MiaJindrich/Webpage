from django.contrib import admin
from app.models import UserProfileInfo, Topic, Article, AccessRecord

admin.site.register(UserProfileInfo)
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(AccessRecord)
