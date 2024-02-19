from django.contrib import admin

# local imports 
from landingpage.models import PersonalDetails, Project, SociaLinks
# Register your models here.
admin.site.register(Project)
admin.site.register(PersonalDetails)
admin.site.register(SociaLinks)
