from django.urls import path
from .apiviews import NotificationsView
urlpatterns = [
    path('notifications/', NotificationsView.as_view(),name="notifications")
]
