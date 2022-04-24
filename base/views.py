from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

channels = [
    {'id': 1, 'name': 'first_militia'},
    {'id': 2, 'name': 'second_militia'},
    {'id': 3, 'name': 'third_militia'},
    {'id': 4, 'name': 'fourth_militia'},
]

def home(request):
    context = {'channels': channels}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')
