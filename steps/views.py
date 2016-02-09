from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.utils.html import escape, strip_tags
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from models import StepCount
from django.core.mail import send_mass_mail
from django.conf import settings


# Create your views here.


# renders the index page
def index(request):
    date, day = get_date(10)
    time = date.strftime('%d/%m/%Y')

    if request.user.is_authenticated():
        s = get_user_steps(request.user, date)
        if s is None:
            steps = ""
        else:
            steps = str(s.steps)
    else:
        steps = ""

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

# send emails to all groups
def send_emails(request):
    one, two, three = separate()
    print one
    to_email_one = email_one(one)
    print to_email_one
    # send_mass_mail(to_email_one)
    return HttpResponse("Done!")


# Group 1: Control Group
# Group 2: Inter-pair competition
# Group 3: Competition amongst all pairs

# separate the groups
def separate():
    one = []
    two = []
    three = []
    users = User.objects.all()
    for u in users:
        user_id = int(u.username)
        if user_id >= 11 and user_id <= 100:
            one.append(u)
        elif user_id >= 101 and user_id <= 200:
            two.append(u)
        elif user_id >= 201 and user_id <= 300:
            three.append(u)

    return one, two, three


# generates email responses for group 1
def email_one(users):
    data = []
    (date, day) = get_date(10)
    date_str = date.strftime('%d/%m/%Y')
    subject = "Steps update for " + date_str
    for u in users:
        s = get_user_steps(u, date)
        if s is None:
            message = "Dear User " + u.username + ", you did not enter data for " + date_str + "."
        else:
            if s.steps >= 10000:
                message = "Congratulations User " + u.username + ", you completed your goal with a total of " + str(s.steps) + " for " + date_str +"."
            else:
                message = "Dear User "+ u.username + ", you did not complete your goal with a total of just " + str(s.steps) + " for " + date_str +"."

    data = tuple(data)
    return data


# generates email responses for group 2
def email_two(users):
    data = []
    (date, day) = get_date(10)
    date_str = date.strftime('%d/%m/%Y')
    subject = "Steps update for " + date_str
    for u in users:
        s = get_user_steps(u, date)
        if s is None:
            message = "Dear User " + u.username + ", you did not enter data for " + date_str + "."
        else:
            if s.steps >= 10000:
                message = "Congratulations User " + u.username + ", you completed your goal with a total of " + str(s.steps) + " for " + date_str +"."
            else:
                message = "Dear User "+ u.username + ", you did not complete your goal with a total of just " + str(s.steps) + " for " + date_str +"."

    data = tuple(data)
    return data