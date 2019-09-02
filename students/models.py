from django.db import models
from django.contrib.auth.models import User
from academics.models import Class, Course
# Create your models here.


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20)
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    course_enrolled = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='profile_image', blank=True)

    class Meta:
        verbose_name = "Student Profile"
        verbose_name_plural = "Student Profiles"

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.user.username
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         StudentProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#         instance.studentprofile.save()
