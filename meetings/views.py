from django.http import HttpResponse, Http404
from django.shortcuts import render
from meetings.models import Room, Departments
from django.template import loader


# Create your views here.
def roomlist(request):
    room_list = Room.objects.order_by('room_location').order_by('room_name')
    template = loader.get_template('meetings/roomlist.html')
    context = {'room_list': room_list}

    for room in room_list:
        room.room_department = Departments[room.room_department][1]

    return HttpResponse(template.render(context))


def detail(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
        room.room_department = Departments[room.room_department][1]
    except Room.DoesNotExist:
        raise Http404("Meeting room does not exist")

    return render(request, 'meetings/room.html', {'room': room})