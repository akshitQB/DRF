from django.db import models

class Students(models.Model):
    Roll_no = models.IntegerField()
    F_name = models.CharField(max_length=100)
    L_name = models.CharField(max_length=100)
    

