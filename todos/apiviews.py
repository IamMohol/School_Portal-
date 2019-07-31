from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class TodoView(ListCreateAPIView):
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        todos = Todo.objects.filter(student=self.request.user)
        return todos

    def perform_create(self, serializer):
        creator = get_object_or_404(User, id=self.request.data.get('student'))
        return serializer.save(creator=creator)


class SingleTodoView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Todo.objects.filter(student=self.request.user)
        return queryset

