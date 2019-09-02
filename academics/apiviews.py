from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Course, Class, Unit, UnitDetail, Grade, UnitRegistration, CourseOutline, MyPlate
from . import  serializers


class CoursesList(generics.ListAPIView):
    serializer_class = serializers.CoursesSerializer
    queryset = Course.objects.all()
    
#
# class UnitList(generics.ListAPIView):
#     # authentication_classes = ()
#     # permission_classes = ()
#     queryset = Unit.objects.filter(course_id__course_name="Computer Technology")
#     serializer_class = UnitsSerializer


class UnitsRegisteredView(generics.ListAPIView):
    serializer_class = serializers.UnitsRegisteredSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = self.request.user
        queryset = UnitRegistration.objects.filter(student=student)
        id= self.request.query_params.get("id", None)
        if id:
            queryset = queryset.filter(id=id)
        return queryset


class UnitDetailView(generics.ListAPIView):
    serializer_class = serializers.UnitDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = UnitDetail.objects.all()
        unit_id = self.request.query_params.get("id", None)
        if unit_id:
            queryset = UnitDetail.objects.filter(id=unit_id)

        return queryset


class CourseOutlineView(generics.ListAPIView):
    serializer_class = serializers.CourseOutlineSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseOutline.objects.all()
        unit_id = self.request.query_params.get("id", None)
        if unit_id:
            queryset = CourseOutline.objects.filter(unit__id=unit_id)

        return queryset


class ClassList(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = serializers.ClassSerializer


class Grades(generics.ListCreateAPIView):
    serializer_class = serializers.GradesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        grades = Grade.objects.filter(student=self.request.user)
        year = self.request.query_params.get("year", None)
        if year:
            grades = grades.filter(course_unit__clss__year=year)

        semester = self.request.query_params.get("semester", None)
        if semester:
            grades = grades.filter(course_unit__clss__semester=semester)

        return grades


class MyPlateView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.MyPlateSerializer

    def get_queryset(self):
        class_enrolled = self.request.user.studentprofile.class_enrolled
        query = MyPlate.objects.filter(clss=class_enrolled)

        return query


