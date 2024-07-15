from django.db import models

# Create your models here.
class Stud(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    joining_date = models.DateField()
    #courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Course(models.Model):
    course_name = models.CharField(max_length = 50)
    description = models.TextField()
    students = models.ManyToManyField(Stud, related_name = 'courses')
    teaching_assistant = models.ForeignKey(Stud, on_delete = models.CASCADE, related_name='taught_courses')

    def __str__(self):
        return f"{self.course_name}"