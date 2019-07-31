from rest_framework import serializers 
from rest_framework.authtoken.models import Token 
from rest_framework import exceptions
from django.contrib.auth import authenticate  
from django.contrib.auth.models  import User 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        username = data.get("username","")
        password = data.get("password","")


        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else: 
                msg = "Unable to login with given credentials."
                raise exceptions(msg)
            
        else: 
            msg = "Must provide both username and password"
            raise exceptions(msg)
        return data 