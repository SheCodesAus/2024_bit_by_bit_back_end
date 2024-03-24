from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Events, EventMentors
from .serializers import EventSerializer, EventDetailSerializer, EventMentorsSerializer, EventMentorsDetailSerializer
from rest_framework import status
from django.http import Http404


class EventList(APIView):

    def get(self, request):
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
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
        project = self.get_object(pk)
        serializer = EventDetailSerializer(project)
        return Response(serializer.data)
    

class EventMentorList(APIView):

    def get(self, request):
        eventmentors = EventMentors.objects.all()
        serializer = EventMentorsSerializer(eventmentors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventMentorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(eventmentor_id=request.user)
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
        

