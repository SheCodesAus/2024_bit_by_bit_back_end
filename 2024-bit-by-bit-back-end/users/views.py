from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, UserProcess
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, UserProcessSerializer, UserProcessDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser


class UserList(APIView):
    permission_classes = [permissions.IsAuthenticated]
  
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
class CreateUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CustomUserDetail(APIView):
    # parser_classes = (MultiPartParser, FormParser)
    
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserDetailSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserDetailSerializer(
            instance=user,
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
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserProcessList(APIView):

    def get(self, request):
        user_processes = UserProcess.objects.all()
        serialized_data = UserProcessSerializer(user_processes, many=True).data
        return Response(serialized_data)
    
    def post(self, request):
        # Assuming user_id is a one-to-one relationship with User
        print("request", request)
        request.data['user_id'] = request.user.id
        serializer = UserProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProcessDetail(APIView):
    
    def get_object(self, pk):
        try:
            return UserProcess.objects.get(pk=pk)
        except UserProcess.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserProcessDetailSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserProcessDetailSerializer(
            instance=user,
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
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
