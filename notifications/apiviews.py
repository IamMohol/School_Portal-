from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Notifications
from .serializers import NotificationsSerializer


class NotificationsView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationsSerializer

    def get_queryset(self):
        course_en = self.request.user.studentprofile.course_enrolled
        return Notifications.objects.filter(course=course_en)
