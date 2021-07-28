
from django.shortcuts import render
from .models import Causes

# Create your views here.
def causes(request):

    con = Causes.objects.all()
    context = {
        'causes': con
    }

    
    return render(request, 'causes/causes.html', context)

def causesdetail(request):
    return render(request, 'causes/causesdetail.html')