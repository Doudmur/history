from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from config.views import index, news_page, newsDetailView
from user.views import login, logout, profile, tasks_page, tasksDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tasks/', tasks_page, name='tasks_page'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('news/', news_page, name='news_page'),
    path('news/<int:pk>', newsDetailView.as_view(), name='news_detail'),
    path('tasks/<int:pk>', tasksDetailView.as_view(),name='tasks_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



