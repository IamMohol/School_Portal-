from rest_framework import serializers
from rest_framework.authtoken.models import Token 
from . import models
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User 
#         fields = ('username','email','password', 'registration_number')
#         extra_kwargs = {'password':{'write_only':True}}
    
#     def create (self, validated_data):
#         user = User(
#             email = validated_data['email'],
#             username = validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         Token.objects.create(user=user)
#         return user 


class CoursesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Course
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Class
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Unit
        fields = '__all__'


class UnitDetailSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = models.UnitDetail
        fields = '__all__'


class UnitsRegisteredSerializer(serializers.ModelSerializer):
    unit = UnitDetailSerializer(read_only=True)

    class Meta: 
        model = models.UnitRegistration
        fields = '__all__'


class CourseUnitSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)
    clss = ClassSerializer(read_only=True)

    class Meta:
        model = models.CourseUnit
        fields = '__all__'


class GradesSerializer(serializers.ModelSerializer):
    course_unit = CourseUnitSerializer(read_only=True)

    class Meta: 
        model = models.Grade
        fields = '__all__'


