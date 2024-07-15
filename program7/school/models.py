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

class Project(models.Model):
    student = models.OneToOneField(Stud, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    languages_used = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.topic} by {self.student.fname} {self.student.lname}"