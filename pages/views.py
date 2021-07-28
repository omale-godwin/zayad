from django.shortcuts import render
from .models import Galary
from causes.models import Causes
from event.models import Event
# Create your views here.

def index(request):

    con = Causes.objects.all()[:3]
    cons = Event.objects.all()[:3]
    context = {
        'causes': con,
        'events': cons
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def galary(request):
    gala = Galary.objects.all()

    context = {
        'galary': gala
    }
    return render(request, 'pages/galary.html', context)