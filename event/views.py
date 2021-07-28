from django.shortcuts import render, get_object_or_404
from .models import Event
# Create your views here.
def event(request):
    con = Event.objects.all()
    context = {
        'events': con
    }

    return render(request, 'event/event.html', context)

def eventdetail(request, event_id):

    listing = get_object_or_404(Event, pk=event_id)
    context = {
    'events': listing
    }
    return render(request, 'event/eventdetail.html', context)