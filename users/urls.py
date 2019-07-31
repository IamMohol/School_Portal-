from django.urls import path 
from .apiviews import  LoginView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
