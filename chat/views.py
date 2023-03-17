from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    context_dict = {}

    context_dict['room_name'] = room_name
    return render(request, "chat/room.html", context_dict)
