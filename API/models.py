from django.db import models

class Students(models.Model):
    roll_no = models.IntegerField()
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
