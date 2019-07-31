from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import FinanceSerializer, FinanceHistorySerializer
from .models import Finance, FinanceHistory


class FinanceView(generics.ListAPIView):
    serializer_class = FinanceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = self.request.user
        queryset = Finance.objects.filter(student=student)
        return queryset


class FinanceHistoryView(generics.ListAPIView):
    serializer_class = FinanceHistorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = self.request.user
        queryset = FinanceHistory.objects.filter(student=student)
        return queryset

