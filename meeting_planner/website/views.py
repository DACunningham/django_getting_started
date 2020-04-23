from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.


def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This var is from the View",
                   "num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse(r"<h1>About</h1><i>Name:</i> Dexter Cunningham<br>" +
                        r"<i>Locale:</i> Wiltshire")
