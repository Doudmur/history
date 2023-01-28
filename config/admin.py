from django.contrib import admin
from config.models import news_list
from user.models import Task

admin.site.register(news_list)
admin.site.register(Task)