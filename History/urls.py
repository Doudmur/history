from django.contrib import admin
from django.urls import path
from config.views import index, news_page, newsDetailView
from user.views import login, logout, profile, tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('news/', news_page, name='news_page'),
    path('tasks/', tasks, name='tasks'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('news/<int:pk>', newsDetailView.as_view(), name='news_detail')
]
