from rest_framework import serializers
from .models import Finance, FinanceHistory


class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'


class FinanceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceHistory
        fields = '__all__'


