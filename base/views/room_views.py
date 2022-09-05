from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from base.models import Room
from base.serializers import RoomSerializer

from rest_framework import status


@api_view(['GET'])
def getRooms(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''

    Rooms = Room.objects.filter(
        title__icontains=query).order_by('-price')

    page = request.query_params.get('page')
    paginator = Paginator(Rooms, 10)

    try:
        Rooms = paginator.page(page)
    except PageNotAnInteger:
        Rooms = paginator.page(1)
    except EmptyPage:
        Rooms = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = RoomSerializer(Rooms, many=True)
    return Response({'Rooms': serializer.data, 'page': page, 'pages': paginator.num_pages})


# @api_view(['GET'])
# def getTopRooms(request):
#     Rooms = Room.objects.filter(rating__gte=4).order_by('-rating')[0:5]
#     serializer = RoomSerializer(Rooms, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(_id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createRoom(request):
    user = request.user

    room = Room.objects.create(
        user=user,
        title='Sample title',
        floor=0,
        beds=1,
        room_no=1,
        room_type='Sample',
        tags=['room'],
        price=0,
    )

    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateRoom(request, pk):
    data = request.data
    room = Room.objects.get(_id=pk)

    room.title = data['title']
    room.price = data['price']
    room.floor = data['floor']
    room.beds = data['beds']
    room.room_no = data['room_no']
    room.room_type = data['room_type']
    room.price = data['price']

    room.save()

    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteRoom(request, pk):
    room = Room.objects.get(_id=pk)
    room.delete()
    return Response('Roomed Deleted')


@api_view(['POST'])
def uploadImage(request):
    data = request.data

    Room_id = data['Room_id']
    Room = Room.objects.get(_id=Room_id)

    Room.image = request.FILES.get('image')
    Room.save()

    return Response('Image was uploaded')
