from rest_framework import generics 
from rest_framework.views import  APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from .models import StudentProfile
from .serializers import StudentProfileSerializer

class StudentProfileView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentProfileSerializer

    def get_queryset(self):
        guy = self.request.user
        return StudentProfile.objects.filter(user=guy)
  