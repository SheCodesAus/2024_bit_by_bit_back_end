from django.db import models
from django.contrib.auth import get_user_model


class Events(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    event_type= models.TextField()
    event_name = models.TextField()
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    attendee_numbers = models.IntegerField()
    location = models.TextField()
    event_mentors = models.ForeignKey('EventMentors', on_delete=models.CASCADE, related_name='events', blank=True, null=True)
    is_open = models.BooleanField()
    date_created = models.DateTimeField()


class EventMentors(models.Model):
    eventmentor_id = models.IntegerField()
    event_id = models.ForeignKey('Events', on_delete=models.CASCADE, related_name='event_user')
    mentor_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name= 'mentored_events')
    approved = models.BooleanField(default=False)
    event_onboarding_task = models.IntegerField(blank=True, null=True) 
    event_offboarding_task = models.IntegerField(blank=True, null=True) 
    role_requested = models.BooleanField(default=False)
    role_assigned = models.BooleanField(blank=True, null=True)   
    is_completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


