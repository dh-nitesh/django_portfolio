from django.urls import path

#local imports
from gallery.views import CardView
app_name = 'gallery'

urlpatterns = [
    path('', CardView.as_view(), name='card'),
]