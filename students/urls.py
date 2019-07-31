from django.urls import path 
from .apiviews import StudentProfileView

urlpatterns = [
    path("profile/", StudentProfileView.as_view(),name='profile')
]

