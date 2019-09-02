from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Timetable
from .serializers import TimetableSerializer


class TimetableView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TimetableSerializer

    def get_queryset(self):
        class_enrolled = self.request.user.studentprofile.class_enrolled
        query = Timetable.objects.filter(clss=class_enrolled)
        day = self.request.query_params.get("day", None)

        if day:
            query = query.filter(day=day)

        return query

