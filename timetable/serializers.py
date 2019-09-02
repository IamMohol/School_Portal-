from rest_framework import serializers
from .models import Timetable
from academics.serializers import UnitSerializer


class TimetableSerializer(serializers.ModelSerializer):
    start = serializers.TimeField(format="%H:%M", required=False, read_only=True)
    end = serializers.TimeField(format="%H:%M", required=False, read_only=True)
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = Timetable
        fields = '__all__'

