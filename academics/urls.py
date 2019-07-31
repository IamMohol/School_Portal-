from django.urls import path
from . import apiviews

urlpatterns = [
    path("courses/", apiviews.CoursesList.as_view(), name="courses_list"),
    path('units/', apiviews.UnitsRegisteredView.as_view(), name='units_registered'),
    path('unit/<int:pk>/', apiviews.UnitDetailView.as_view(), name='unit_detail'),
    path("grades/", apiviews.Grades.as_view(), name="grades"),
]