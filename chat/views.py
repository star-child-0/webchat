from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "chat/index.html")


@login_required
def room(request, room_name):
    context_dict = {}

    context_dict['room_name'] = room_name
    return render(request, "chat/room.html", context_dict)
