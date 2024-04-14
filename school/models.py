from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    date_of_enrollment = models.DateField()
    grade = models.DecimalField(max_digits=3, decimal_places=1)
