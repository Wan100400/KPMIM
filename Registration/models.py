from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=4, primary_key = True)
    description = models.TextField()

class Mentor(models.Model):
    mentorCd = models.CharField(max_length=4, primary_key = True)
    mentorName = models.TextField()
    mentorEmail = models.EmailField(default='default@gmail.com')

class Student(models.Model):
    id = models.CharField(max_length=12, primary_key = True)
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 12)
    Course_code = models.ForeignKey(Course, on_delete = models.CASCADE)
    status = models.CharField(max_length=3, default='MP')
