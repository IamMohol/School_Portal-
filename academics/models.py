from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Global Variables
FIRST_YEAR = 1
SECOND_YEAR = 2
THIRD_YEAR = 3
FOURTH_YEAR = 4
FIFTH_YEAR = 5
SIXTH_YEAR = 6
YEARS = (
    (FIRST_YEAR, 'First Year'),
    (SECOND_YEAR, 'Second Year'),
    (THIRD_YEAR, 'Third Year'),
    (FOURTH_YEAR, 'Fourth Year'),
    (FIFTH_YEAR, 'Fifth Year'),
    (SIXTH_YEAR, 'Sixth Year'),
)
# Semester choice fields 
FIRST_SEM = 1
SECOND_SEM = 2
THIRD_SEM = 3
SEMESTERS = (
    (FIRST_SEM, 'First Semeseter'),
    (SECOND_SEM, 'Second Semester'),
    (THIRD_SEM, 'Third Semeseter'),
)

# Grade choices 
A = 1
B = 2
C = 3
D = 4
E = 5
GRADES = (
    (A, 'A',),
    (B, 'B',),
    (C, 'C',),
    (D, 'D',),
    (E, 'E - FAIL',),
)


# Courses Table that holds every course registered for the system
class Course(models.Model):
    course_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.course_name


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField(choices=YEARS, default=None)
    semester = models.IntegerField(choices=SEMESTERS, default=None)

    class Meta:
        verbose_name_plural = 'Classes'
        constraints = [models.UniqueConstraint(fields=['course', 'year', 'semester'], name='Unique Classes')]

    def __str__(self):
        return '{} {}.{}'.format(
            self.course,
            self.year,
            self.semester
        )

    def get_absolute_url(self):
        pass


# Defines the Units Table is related to the course table a unit may be in several courses
class Unit(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CourseUnit(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    clss = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.clss, self.unit)


class Lecturer(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return "{} {}".format(
            self.f_name,
            self.l_name
        )


class UnitDetail(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    description = models.TextField()
    course_outline = models.TextField()
    resources = models.CharField(max_length=100, blank=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, blank=True, null=True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    difficulty = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.unit.name


class Grade(models.Model):
    midterm_mark = models.FloatField()
    final_mark = models.FloatField()
    grade = models.CharField(default=None, max_length=10)
    course_unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['student', 'course_unit'], name="Unique Grades")]

    def __str__(self):
        return '{} - [{}]'.format(
            self.student,
            self.course_unit
        )

    def get_absolute_url(self):
        pass


class Goal(models.Model):
    pass


class UnitRegistration(models.Model):
    unit = models.ForeignKey(UnitDetail, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Unit registration'

    def __str__(self):
        return '{}({})'.format(
            self.unit,
            self.student
        )


class CourseOutline(models.Model):
    unit = models.ForeignKey(UnitRegistration, on_delete=models.CASCADE)
    week = models.CharField(max_length=10)
    content = models.CharField(max_length=500)

    def __str__(self):
        return "{} {}".format(
            self.unit,
            self.week
        )


class MyPlate(models.Model):
    type = models.CharField(max_length=15)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    lec = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    clss = models.ForeignKey(Class, on_delete=models.CASCADE)
    due_date = models.DateTimeField()

    def __str__(self):
        return '{} {} {}'.format(
            self.type,
            self.unit.name,
            self.due_date,
        )
