from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profilepic = models.ImageField()
    bio = models.CharField(max_length=300)
    coding_language = models.TextField()
    linkedin = models.URLField()
    contact_number = models.IntegerField()
    is_admin = models.BooleanField(default=False) 
    def __str__(self):
        return self.username


class UserProcess(models.Model):
    userprocess_id = models.IntegerField() 
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    user_onboarding_task = models.IntegerField(blank=True, null=True)  
    user_offboarding_task = models.IntegerField(blank=True, null=True)   
    is_completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


