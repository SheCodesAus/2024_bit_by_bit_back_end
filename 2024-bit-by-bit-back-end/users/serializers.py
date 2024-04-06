from rest_framework import serializers
from .models import CustomUser, UserProcess


class UserProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProcess
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CustomUserDetailSerializer(serializers.ModelSerializer):
    onboarded_mentor = UserProcessSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

class UserProcessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProcess
        fields = '__all__'

    
