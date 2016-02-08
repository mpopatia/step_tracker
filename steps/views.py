from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.utils.html import escape, strip_tags
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from models import StepCount
import json

# Create your views here.


def get_date(threshold):
    now = datetime.now()
    today_threshold_am = now.replace(hour=threshold, minute=0, second=0, microsecond=0)
    if now < today_threshold_am:
        time = date.today() - timedelta(days=1)
        day = "yesterday"
    else:
        time = date.today()
        day = "today"

    return time, day


def index(request):
    time, day = get_date(10)
    time = time.strftime('%d/%m/%Y')
    return render(request, 'steps/index.html', {"loggedin": request.user.is_authenticated, "time": time, "day": day})


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


def store_steps(request):
    steps = int(escape(strip_tags(request.GET['step_count'])))
    print "STEPS:",steps
    (date, day) = get_date(10)
    s = StepCount.objects.filter(owner=request.user, dateCreated=date)
    if s:
        s = s[0]
        print "Already exists"
        s.steps = steps
        s.save()
    else:
        print "Creating a new one"
        s = StepCount(owner=request.user, dateCreated=date, steps=steps)
        s.save()

    message = "Your response has been recorded. Thank you."
    return HttpResponse(json.dumps(message), content_type = "application/json")