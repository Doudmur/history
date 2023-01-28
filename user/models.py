from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    grade = models.IntegerField(default=11)
    grade_letter = models.CharField(max_length=5, default='Г')


class Task(models.Model):
   title = models.TextField()
   upload_date = models.DateField(auto_now_add=True)
   deadline = models.DateField(null=True, blank=True)
   download_file = models.ImageField()
   upload_file = models.ImageField(null=True, blank=True)
