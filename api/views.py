# # from django.shortcuts import render
# # from rest_framework import generics, status
# # from .serialisers import RoomSerialiser, CreateRoomSerialiser
# # from .models import Room
# # from rest_framework.views import APIView
# # from rest_framework.response import Response


# # # Create your views here.

# # class RoomView(generics.ListCreateAPIView):
# #     queryset = Room.objects.all()
# #     serializer_class = RoomSerialiser

# # class CreateRoomView(APIView):
# #     serialiser_class = CreateRoomSerialiser

# #     def post(self, request, format=None):
# #         if not self.request.session.exists(self.request.session.session_key):
# #             self.request.session.create()

# #         serialiser = self.serialiser_class(data=request.data)
# #         if serialiser.is_valid():
# #             guest_can_pause = serialiser.data.get('guest_can_pause')
# #             votes_to_skip = serialiser.data.get('votes_to_skip')
# #             host = self.request.session.session_key
# #             queryset = Room.objects.filter(host=host)
# #             if queryset.exists():
# #                 room = queryset[0]
# #                 room.guest_can_pause = guest_can_pause
# #                 room.votes_to_skip = votes_to_skip
# #                 room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
# #             else:
# #                 room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
# #                 room.save()

# #             return Response(RoomSerialiser(room).data, status=status.HTTP_201_CREATED)


# from django.shortcuts import render
# from rest_framework import generics, status
# from .serialisers import RoomSerialiser, CreateRoomSerialiser
# from .models import Room
# from rest_framework.views import APIView
# from rest_framework.response import Response


# # Create your views here.


# class RoomView(generics.ListAPIView):
#     queryset = Room.objects.all()
#     serialiser_class = RoomSerialiser

# class CreateRoomView(APIView):
#     def get(self, request, format=None):
#         rooms = Room.objects.all()
#         serialiser = RoomSerialiser(rooms, many=True)
#         return Response(serialiser.data)

#     def post(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         serialiser = CreateRoomSerialiser(data=request.data)
#         if serialiser.is_valid():
#             guest_can_pause = serialiser.data.get('guest_can_pause')
#             votes_to_skip = serialiser.data.get('votes_to_skip')
#             host = self.request.session.session_key
#             queryset = Room.objects.filter(host=host)
#             if queryset.exists():
#                 room = queryset[0]
#                 room.guest_can_pause = guest_can_pause
#                 room.votes_to_skip = votes_to_skip
#                 room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
#                 return Response(RoomSerialiser(room).data, status=status.HTTP_200_OK)
#             else:
#                 room = Room(host=host, guest_can_pause=guest_can_pause,
#                         votes_to_skip=votes_to_skip)
#                 room.save()
# # class CreateRoomView(APIView):
# #     serialiser_class = CreateRoomSerialiser

# #     def get(self, request, format=None):
# #         rooms = Room.objects.all()
# #         serializer = RoomSerialiser(rooms, many=True)
# #         return Response(serializer.data)

# #     def post(self, request, format=None):
# #         if not self.request.session.exists(self.request.session.session_key):
# #             self.request.session.create()

# #         serialiser = self.serialiser_class(data=request.data)
# #         if serialiser.is_valid():
# #             guest_can_pause = serialiser.data.get('guest_can_pause')
# #             votes_to_skip = serialiser.data.get('votes_to_skip')
# #             host = self.request.session.session_key
# #             queryset = Room.objects.filter(host=host)
# #             if queryset.exists():
# #                 room = queryset[0]
# #                 room.guest_can_pause = guest_can_pause
# #                 room.votes_to_skip = votes_to_skip
# #                 room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
# #                 return Response(RoomSerialiser(room).data, status=status.HTTP_200_OK)
# #             else:
# #                 room = Room(host=host, guest_can_pause=guest_can_pause,
# #                             votes_to_skip=votes_to_skip)
# #                 room.save()
#                 return Response(RoomSerialiser(room).data, status=status.HTTP_201_CREATED)

#         return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render
from rest_framework import generics, status
from .serialisers import RoomSerialiser, CreateRoomSerialiser
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerialiser


class CreateRoomView(APIView):
    serializer_class = CreateRoomSerialiser

    def get(self, request, format=None):
        rooms = Room.objects.all()
        serialiser = RoomSerialiser(rooms, many=True)
        return Response(serialiser.data)

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(RoomSerialiser(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
                return Response(RoomSerialiser(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
