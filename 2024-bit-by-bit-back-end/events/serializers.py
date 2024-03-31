from rest_framework import serializers
from .models import Events, EventMentors


class EventMentorsSerializer(serializers.ModelSerializer):
            
      class Meta:
        model = EventMentors
        fields = '__all__'

        
class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    
    class Meta:
        model = Events
        fields = '__all__'



class EventDetailSerializer(EventSerializer):
    mentors = EventMentorsSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')

    def update(self, instance, validated_data):
        instance.event_type = validated_data.get('event_type', instance.event_type)
        instance.event_name = validated_data.get('event_name', instance.event_name)
        instance.event_start_date = validated_data.get('event_start_date', instance.event_start_date)
        instance.event_end_date = validated_data.get('event_end_date', instance.event_end_date)
        instance.attendee_numbers = validated_data.get('attendee_numbers', instance.attendee_numbers)
        instance.location = validated_data.get('location', instance.location)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
    
class EventMentorsDetailSerializer(EventMentorsSerializer):
    event = EventSerializer(many=True, read_only=True)

    class Meta:
        model = EventMentors
        fields = '__all__'
    