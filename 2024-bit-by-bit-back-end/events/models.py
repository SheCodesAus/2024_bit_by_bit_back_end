from django.db import models
from django.contrib.auth import get_user_model


class Events(models.Model):
    event_type= models.TextField()
    event_name = models.TextField()
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    attendee_numbers = models.IntegerField()
    location = models.TextField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_events'
    )



class EventMentors(models.Model):
    event_id = models.ForeignKey('Events', on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='mentors')
    approved = models.BooleanField(default=False)
    event_onboarding_task = models.TextField(blank=True, null=True) 
    event_offboarding_task = models.TextField(blank=True, null=True) 
    role_requested = models.BooleanField(default=False)
    role_assigned = models.BooleanField(blank=True, null=True)   
    is_completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


