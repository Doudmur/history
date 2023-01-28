from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DetailView

from user.forms import LoginForm
from django.contrib import auth
from django.urls import reverse
from user.models import Task

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return login(request)

def tasks_page(request):
    if request.user.is_authenticated:
        context = {
            'tasks': reversed(Task.objects.all())
        }
        return render(request, 'tasks.html', context=context)
    else:
        return login(request)

class tasksDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'tasks'

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

