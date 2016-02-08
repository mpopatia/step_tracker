from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.utils.html import escape, strip_tags
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'steps/index.html', {"loggedin": request.user.is_authenticated})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    user_id = escape(strip_tags(request.POST['user_id']))
    password = escape(strip_tags(request.POST['password']))
    user = authenticate(username = user_id, password = password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("Disabled account")
    else:
        return HttpResponse("Invalid login")


def signup(request):
    user_id = escape(strip_tags(request.POST['user_id']))
    email = escape(strip_tags(request.POST['email']))
    password = escape(strip_tags(request.POST['password']))
    User.objects.create_user(username=user_id, email=email, password=password)
    return HttpResponseRedirect(reverse('index'))