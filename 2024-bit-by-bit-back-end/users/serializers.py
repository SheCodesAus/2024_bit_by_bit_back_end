from rest_framework import serializers
from .models import CustomUser, UserProcess


class CustomUserSerializer(serializers.ModelSerializer):
    profilepic = serializers.ImageField(required=False)
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
class UserProcessSerializer(serializers.ModelSerializer):
    mentors = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = UserProcess
        fields = '__all__'
    
class UserProcessDetailSerializer(serializers.ModelSerializer):
    mentor = UserProcessSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.mentor = validated_data.get('mentor', instance.mentor)
        instance.user_onboarding_task_slack = validated_data.get('user_onboarding_task_slack', instance.user_onboarding_task_slack)
        instance.user_onboarding_task_linkedin = validated_data.get('user_onboarding_task_linkedin', instance.user_onboarding_task_linkedin)
        instance.user_onboarding_task_CodeofConduct = validated_data.get('user_onboarding_task_CodeofConduct', instance.user_onboarding_task_CodeofConduct)
        instance.user_onboarding_task_tshirtsent = validated_data.get('user_onboarding_task_tshirtsent', instance.user_onboarding_task_tshirtsent)
        instance.user_offboarding_task_feedbackrequested = validated_data.get('user_offboarding_task_feedbackrequested', instance.user_offboarding_task_feedbackrequested)
        instance.user_offboarding_task_feedbackreceived = validated_data.get('user_offboarding_task_feedbackreceived', instance.user_offboarding_task_feedbackreceived)
        instance.user_offboarding_task_tshirtreceived = validated_data.get('user_offboarding_task_tshirtreceived', instance.user_offboarding_task_tshirtreceived)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.save()
        return instance

    
