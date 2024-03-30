from rest_framework import serializers
from .models import CustomUser, UserProcess


class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
class UserProcessSerializer(serializers.ModelSerializer):
    mentor = CustomUserSerializer(many=True, read_only=True)  

    class Meta:
        model = UserProcess
        fields = '__all__'
    

    
