from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Events
from .serializers import EventSerializer, EventMentorsSerializer, EventsDetailSerializer, EventMentorsDetailSerializer
from django.http import Http404
from rest_framework import status


class EventList(APIView):

    def get(self, request):
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
class CreateEvent(APIView):

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
    )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
        

class EventDetail(APIView):


    def get_object(self, pk):
        try:
            event = Events.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Events.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventsDetailSerializer(event)
        return Response(serializer.data)

    # Update Projects
    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventsDetailSerializer(
            instance=event,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
    )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(status=status.HTTP_200_OK)