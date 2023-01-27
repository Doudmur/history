from django.shortcuts import render, HttpResponseRedirect
from user.forms import LoginForm
from django.contrib import auth
from django.urls import reverse

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return login(request)

def tasks(request):
    if request.user.is_authenticated:
        return render(request, 'tasks.html')
    else:
        return login(request)

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
