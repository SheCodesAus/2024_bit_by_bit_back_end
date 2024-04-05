from rest_framework import serializers
from .models import CustomUser, UserProcess

class UserProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProcess
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    onboarded_mentor = UserProcessSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):

    # mentor = UserProcessSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.user_id  = validated_data.get('user_id', instance.user_id)
        instance.user_onboarding_task = validated_data.get('user_onboarding_task', instance.user_onboarding_task)
        instance.user_offboarding_task = validated_data.get('user_offboarding_task', instance.user_offboarding_task)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.save()
        return instance

