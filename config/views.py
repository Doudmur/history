from django.shortcuts import render
from config.models import news_list
from django.views.generic import DetailView


def index(request):
    return render(request, 'index.html')


def news_page(request):
    context = {
        'news': reversed(news_list.objects.all())
    }
    return render(request, 'news.html', context=context)

class newsDetailView(DetailView):
    model = news_list
    template_name = 'single_news.html'
    context_object_name = 'news'

