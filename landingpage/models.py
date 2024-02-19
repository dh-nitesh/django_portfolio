from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    heading = models.CharField(max_length=55, default="I forgot to add heading..", blank=False, null=False)
    body = models.TextField(max_length=999, default="", null=True, blank=True)
    start_date = models.DateField(default=timezone.now, null=False, blank=False)
    link = models.URLField(max_length=200, default="", null=True, blank=True)
    end_date = models.DateField(default=timezone.now, null=False, blank=False)
    
    
    def __str__(self) -> str:
        return f"{self.heading}.. start: {self.start_date}, end:{self.end_date}"
    

class PersonalDetails(models.Model):
    name = models.CharField(max_length=55, blank=False, null=False)
    email = models.EmailField(max_length=55, blank=False, null=False)
    phone = models.CharField(max_length=55, blank=False, null=False)
    address = models.CharField(max_length=55, blank=False, null=False)
    about = models.TextField(max_length=999, blank=False, null=False)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"{self.name}.. email: {self.email}, phone:{self.phone}"
    
    @property
    def get_profile_picture(self):
        return f'{settings.SITE_URL}{self.profile_pic.url}'
    

class SociaLinks(models.Model):
    facebook = models.URLField(max_length=200, default="", null=True, blank=True)
    twitter = models.URLField(max_length=200, default="", null=True, blank=True)
    instagram = models.URLField(max_length=200, default="", null=True, blank=True)
    linkedin = models.URLField(max_length=200, default="", null=True, blank=True)
    github = models.URLField(max_length=200, default="", null=True, blank=True)
    youtube = models.URLField(max_length=200, default="", null=True, blank=True)
