from typing import List
from django.shortcuts import render
from django.views.generic import ListView, View
# local imports
from django.forms.models import model_to_dict

# general imports
from collections import defaultdict
from gallery.models import Gallery

from landingpage.models import PersonalDetails

# Create your views here.

class CardView(View):
    template_name = 'timeline/card_list_view.html'
    def get(self, request):
        personal_details = PersonalDetails.objects.filter(is_active=True).last()
        gallery = Gallery.objects.filter(is_active=True)
        return render(request, template_name=self.template_name, context={'gallery': gallery, 'personal_details': personal_details})
