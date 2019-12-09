from django.shortcuts import render

from django.shortcuts import get_object_or_404

# Create your views here.

from django.shortcuts import redirect 
from django.http import HttpResponse 
from .models import Squirrel 
from .forms import SquirrelForm 
import random
# Create your views here.

def all_squir(request):

    squirrels = Squirrel.objects.all()
    #context = [i.unique_squirrel_id+', ' for i in squirrels]
    context = {
             'squirrels':squirrels,
            }
    return render(request, 'sightings/all.html',context)
    #return HttpResponse(context)

# def squi_detail(request, s_id):
#     squir = Squirrel.objects.get(pk=s_id)
#     context = {
#         'squir':squir,
#     }

#     return render(request,'sightings/detail.html',context)

def edit_squir(request, sid):
    squir = get_object_or_404(Squirrel, pk=sid)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = squir)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{sid}')
    else:
        form = SquirrelForm(instance = squir)
    context = {
        'form':form
    }
    return render(request, 'sightings/edit.html',context)


def add_a_squir(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')

    else:
        form = SquirrelForm()

    context = {
        'form': form,
        }
    return render(request, 'sightings/edit.html', context)


def squir_stats(request):

    squirrels = Squirrel.objects.all()
    AM_count = 0
    PM_count = 0
    Age_count = 0
    Loc_count = 0
    Eat_count = 0
    Runs_count = 0
    Forage_count = 0
    total = 0
    for s in squirrels:
        total += 1
        if s.shift == 'AM':
            AM_count += 1
        else:
            PM_count += 1
        if s.age == 'Juvenile':
            Age_count +=1
        if s.location == 'Ground Plane':
            Loc_count +=1
        if s.eating is True:
            Eat_count +=1
        if s.running is True:
            Runs_count +=1
        if s.foraging is True:
            Forage_count +=1
    AM = AM_count/total
    PM = PM_count/total
    Age = Age_count/total
    Loc = Loc_count/total
    Eat = Eat_count/total
    Runs = Runs_count/total
    Forage = Forage_count/total


    context = {
            'squirrels':squirrels,
            'total':total,
            'AM_count':AM_count,
            'Age_count':Age_count,
            'Loc_count':Loc_count,
            'Eat_count':Eat_count,
            'Runs_count':Runs_count,
            'AM':AM,
            'PM':PM,
            'Age':Age,
            'Loc':Loc,
            'Eat':Eat,
            'Runs':Runs,
            'Forage':Forage,

            }

    return render(request, 'sightings/stats.html',context)

def squirrel_location(request):
    sightings = Squirrel.objects.all()
    sightings = random.choices(sightings, k=100)

    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/map.html', context)


def home(request):
    return render(request,'sightings/home.html')
