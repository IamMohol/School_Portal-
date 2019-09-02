from django.urls import path
from .apiviews import TimetableView

urlpatterns = [
    path('timetable/', TimetableView.as_view(), name='timetable')
]
