from django.shortcuts import render
from django.http import JsonResponse
import json
from api.models import room,log
from api.serializers import roomSerializer,logSerializer,roomSerializerClient
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

def index(request):
    room_id = room.objects.all()
    log_id = log.objects.all()
    context = {
    'title' : 'INDEX | MYSMS',
    'room_id' : room_id,
    'log_id' : log_id,

    }   
    return render(request,'index.html',context)

@api_view(['GET'])
def get_room(request):
     rooms = room.objects.all()
     serializer = roomSerializer(rooms, many=True)
     return Response(serializer.data)


@api_view(['GET'])
def get_log(request):
     rooms = log.objects.all()
     serializer = logSerializer(rooms, many=True)
     return Response(serializer.data)

@api_view(['POST', 'GET'])
def updateroom(request):

# ini untuk ip
    if request.method == 'POST':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        data = request.body
        json_data = json.loads(data)

        roomname = room.objects.get(room = json_data['room'])
        log.room = roomname
        log.status = json_data['status']
        room.objects.filter(room = json_data['room']).update(status = json_data['status'])
        log.objects.create(room = roomname, status = json_data['status'],ipaddress = ip)
        return Response(json_data, status = status.HTTP_201_CREATED)
    
    elif request.method == 'GET':
        # data = 'hello world'
        roomname = room.objects.all()
        rooms = room.objects.filter(status = 0)
        if room.objects.filter(status = 1):
            return Response(None)
        else:
            serializer = roomSerializer(rooms, many=True)
            # print(data)
            data = serializer.data
            return Response(data)

# end of room update

def getlog(request):
    log_id = reversed(log.objects.all())
    context = {
    'title' : 'INDEX | MYSMS',
    'log_id' : log_id,

    }   
    return render(request,'getlog.html',context)

def map(request):
    return render(request,'map.html')


@api_view(['GET'])
def loadroom(request):
    data = request.body
    json_data = json.loads(data)
    print(json_data['room'])
    roomname = room.objects.filter(room = json_data['room'])
    # print(roomname)
    serializer = roomSerializerClient(roomname, many=True)
    result = serializer.data
    return Response(result)