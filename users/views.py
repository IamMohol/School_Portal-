import datetime

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        isManager = 0
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)
        name = user.get_full_name() or user.username

        return Response({
            'token': token.key,
            'name': name,
            'user_id': user.pk,
            'email': user.email,
        })
