from django.contrib import admin
from academics import models
# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Unit)
admin.site.register(models.UnitDetail)
admin.site.register(models.Class)
admin.site.register(models.Grade)
admin.site.register(models.CourseUnit)
admin.site.register(models.UnitRegistration)
admin.site.register(models.Lecturer)
admin.site.register(models.CourseOutline)
admin.site.register(models.MyPlate)
