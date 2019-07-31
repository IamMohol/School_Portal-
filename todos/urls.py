from django.urls import path
from .apiviews import TodoView

urlpatterns = [
    path('todos/', TodoView.as_view(), name='todos'),
    path('todos/<int:pk>', TodoView.as_view(), name='todoDetail'),
]
