from django.db import models

class Student(models.Model):
    gr_no = models.IntegerField()
    stu_name = models.CharField(max_length=50)
    stu_class = models.CharField(max_length=50)
    stu_email = models.EmailField()