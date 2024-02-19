from django.urls import path

#local imports
from landingpage.views import  HomePageView

urlpatterns = [
    # path('', landingpage_views.ProjectView.as_view(), name='project'),
    path('', HomePageView.as_view(), name='home'),
]