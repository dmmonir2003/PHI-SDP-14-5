from django.db import models

# Create your models here.


class StudentModel(models.Model):
    name=models.TextField()
    roll=models.IntegerField(default=1)

