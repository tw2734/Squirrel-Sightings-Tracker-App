from django.shortcuts import render
from .models import Squirrel
import random

# Create your views here.

def squirrel_location(request):
    sightings = Squirrel.objects.all()
    sightings = random.choices(sightings, k=100)

    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/map.html', context)

