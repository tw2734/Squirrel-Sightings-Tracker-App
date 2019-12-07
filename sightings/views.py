from django.shortcuts import render

from .models import Squirrel

# Create your views here.

def squirrel_location(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/map.html', context)

