from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import StudentProfile
from academics import serializers as a_serial

# This is the Main Profile Serializer that processes and formats the user and student information and returns the appropriate fields

class StudentProfileSerializer(serializers.ModelSerializer):
    # Related Fields
    username = serializers.ReadOnlyField(source='user.username')
    first_name= serializers.ReadOnlyField(source='user.first_name')
    l_name = serializers.ReadOnlyField(source='user.last_name')
    class_enrolled = a_serial.ClassSerializer(read_only=True)
    course_enrolled = a_serial.CoursesSerializer(read_only=True)

    class Meta: 
        model = StudentProfile
        fields = ( '__all__')