# from django.db import models
# from academics.models import Class, Unit
#
#
# # Create your models here.
# class Timetable(models.Model):
#     unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     venue = models.CharField(max_length=20)
#     clss = models.ForeignKey(Class, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return '{}({})----({})-({})'.format(
#             self.unit,
#             self.venue,
#             self.start_time,
#             self.end_time
#         )
#
