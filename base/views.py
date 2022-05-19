from django.shortcuts import render
from django.http import HttpResponse


channels = [
    {'id': 1, 'name': 'first_militia'},
    {'id': 2, 'name': 'second_militia'},
    {'id': 3, 'name': 'third_militia'},
    {'id': 4, 'name': 'fourth_militia'},
]


def home(request):
    context = {'channels': channels}
    return render(request, 'base/home.html', context)


def channel(request, key):
    current_channel = None
    for i in channels:
        if i['id'] == int(key):
            current_channel = i
    context = {'current_channel': current_channel}
    return render(request, 'base/channel.html', context)
