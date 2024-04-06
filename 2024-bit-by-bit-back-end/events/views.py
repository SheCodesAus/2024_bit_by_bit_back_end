from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Events, EventMentors
from .serializers import EventSerializer, EventDetailSerializer, EventMentorsSerializer, EventMentorsDetailSerializer
from django.http import Http404
from rest_framework import status, permissions




class EventList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            event = Events.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Events.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        event = self.get_object(pk)
        # Fetch related mentors for the event
        mentors = event.eventmentors_set.all()
        serializer = EventDetailSerializer(event)
        data = serializer.data
        # Add mentors data to the serialized event data
        data['mentors'] = EventMentorsSerializer(mentors, many=True).data
        return Response(data)
 
    def put(self,request,pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(
            instance=event,
            data=request.data,
            partial=True
        )
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_200_OK)

class EventMentorList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            eventmentor = Events.objects.get(pk=pk)
            self.check_object_permissions(self.request, eventmentor)
            return eventmentor
        except Events.DoesNotExist:
            raise Http404

    def get(self, request):
        eventmentor = EventMentors.objects.all()
        serializer = EventMentorsSerializer(eventmentor, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Pass the user ID directly to the mentor_id field
        request.data['mentor_id'] = request.user.id
        serializer = EventMentorsSerializer(data=request.data)
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
    
class EventMentorDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            eventmentor = EventMentors.objects.get(pk=pk)
            self.check_object_permissions(self.request, eventmentor)
            return eventmentor
        except EventMentors.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        eventmentor = self.get_object(pk)
        serializer = EventMentorsDetailSerializer(eventmentor)
        return Response(serializer.data)
    
    def put(self, request, pk):
        mentor = self.get_object(pk)
        serializer = EventMentorsDetailSerializer(
            instance=mentor,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_200_OK)


    
        

