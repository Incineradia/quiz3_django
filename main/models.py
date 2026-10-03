from django.db import models

# Create your models here.
class Students(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    codename=models.CharField(max_length=25)
    section=models.CharField(max_length=25)