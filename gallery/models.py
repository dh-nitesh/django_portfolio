from django.conf import settings
from django.db import models 
from django.utils import timezone


class Gallery(models.Model):
    title = models.CharField(max_length=55, default="I forgot to add title..", blank=False, null=False)
    description = models.TextField(max_length=999, default="", null=True, blank=True)
    image = models.ImageField(upload_to='gallery_pics/', blank=True, null=True)
    created_at = models.DateField(default=timezone.now, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    
    
    def __str__(self) -> str:
        return f"{self.title}.. created: {self.created_at}"
    
    @property
    def get_image(self):
        return f'{settings.SITE_URL}{self.image.url}'