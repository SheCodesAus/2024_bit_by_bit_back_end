from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, UserProcess
from .serializers import CustomUserSerializer, UserProcessSerializer, CustomUserDetailSerializer
from rest_framework import status
from django.http import Http404


class UserList(APIView):

    def get(self, request):
        events = CustomUser.objects.all()
        serializer = CustomUserSerializer(events, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
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
    

class CustomUserDetail(APIView):

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
class UserProcessList(APIView):

    def get(self, request):
        user_process = UserProcess.objects.all()
        serializer = UserProcessSerializer(user_process, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Assuming user_id is a one-to-one relationship with User
        print("request", request)
        request.data['user_id'] = request.user.id
        serializer = UserProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

