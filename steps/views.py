from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.utils.html import escape, strip_tags
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from models import StepCount


# Create your views here.


# renders the index page
def index(request):
    date, day = get_date(10)
    time = date.strftime('%d/%m/%Y')

    s = get_user_steps(request.user, date)
    if s is None:
        steps = ""
    else:
        steps = str(s.steps)

    return render(request, 'steps/index.html', {"loggedin": request.user.is_authenticated, "time": time, "day": day, "steps": steps})


# logs the user out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# logs the user in
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


# creates a new user
def signup(request):
    user_id = escape(strip_tags(request.POST['user_id']))
    email = escape(strip_tags(request.POST['email']))
    password = escape(strip_tags(request.POST['password']))
    User.objects.create_user(username=user_id, email=email, password=password)
    return HttpResponseRedirect(reverse('index'))


# renders the success notification page
def success(request):
    message = "Your response has been recorded. Thank you."
    return render(request, 'steps/success.html', {"loggedin": request.user.is_authenticated, "message": message})


# stores the step count for the user
def store_steps(request):
    steps = int(escape(strip_tags(request.GET['step_count'])))
    print "STEPS:",steps
    (date, day) = get_date(10)
    s = get_user_steps(request.user, date)
    if s is None:
        s = StepCount(owner=request.user, dateCreated=date, steps=steps)
        s.save()
    else:
        s.steps = steps
        s.save()

    return HttpResponseRedirect(reverse('success'))


# returns the user object for the current date if one exists
def get_user_steps(user, date):
    s = StepCount.objects.filter(owner=user, dateCreated=date)
    if s:
        s = s[0]
        print "Already exists"
        return s
    else:
        print "Need to create a new one"
        return None


# returns the date for which data is being entered
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