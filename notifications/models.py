from django.db import models
from academics.models import Course


# Create your models here.
class Notifications(models.Model):
    text = models.TextField()
    date_posted = models.DateField()
    time_posted = models.TimeField(null=True, blank=True)
    avatar = models.ImageField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        if len(self.text) >= 80:
            return self.text[:80] + "..."
        else:
            return self.text
