from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Todo(models.Model):
    item = models.TextField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
