from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    profilepic = models.ImageField(blank=True, null=True)
    bio = models.CharField(max_length=300)
    coding_language = models.TextField()
    contact_number = models.CharField(max_length=20, null=True)
    slack = models.CharField(max_length=100,blank=True, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    is_admin = models.BooleanField(default=False)
     
    def __str__(self):
        return self.username


class UserProcess(models.Model):
    mentor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='onboarded_mentor')
    user_onboarding_task = models.TextField(blank=True, null=True)  
    user_offboarding_task = models.TextField(blank=True, null=True)   
    is_completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


