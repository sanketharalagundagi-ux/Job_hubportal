from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPES = [
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='job_seeker')
    phone = models.CharField(max_length=15, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username