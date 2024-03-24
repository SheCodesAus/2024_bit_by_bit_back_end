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

    class Meta:
        model = UserProcess
        fields = '__all__'

class CustomUserDetailSerializer(CustomUserSerializer):
    user_signup = UserProcessSerializer(read_only=True)

    def update(self, instance, validated_data):
        instance.event_type = validated_data.get('event_type', instance.event_type)
        instance.event_name = validated_data.get('event_name',
    instance.event_name)
        instance.event_start_date = validated_data.get('event_start_date', instance.event_start_date)
        instance.event_end_date = validated_data.get('event_end_date', instance.event_end_date)
        instance.attendee_numbers = validated_data.get('attendee_numbers', instance.attendee_numbers)
        instance.location= validated_data.get('location', instance.location)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.save()
        return instance
    
class UserProcessDetailSerializer(UserProcessSerializer):
    user = CustomUserSerializer(read_only=True)

    def update(self, instance, validated_data):
        instance.event_id  = validated_data.get('event_id ', instance.event_id)
        instance.mentor_id  = validated_data.get('mentor_id ', instance.mentor_id )
        instance.approved = validated_data.get('approved', instance.approved)
        instance.event_onboarding_task = validated_data.get('event_onboarding_task', instance.event_onboarding_task)
        instance.event_offboarding_task = validated_data.get('event_offboarding_task', instance.event_offboarding_task)
        instance.role_requested = validated_data.get('role_requested', instance.role_requested)
        instance.role_assigned = validated_data.get('role_assigned', instance.role_assigned)
        instance.save()
        return instance


