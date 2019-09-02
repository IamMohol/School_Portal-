from django.db import models
from academics.models import Class, Unit


# Create your models here.
class Timetable(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    day = models.CharField(max_length=50, blank=True, null=True)
    start = models.TimeField()
    end = models.TimeField()
    venue = models.CharField(max_length=20)
    clss = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Timetable'

    def __str__(self):
        return '{}({})----({})-({})'.format(
            self.unit,
            self.venue,
            self.start,
            self.end
        )


