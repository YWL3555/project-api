from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tourGuide = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()

class TourGuide(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    email = models.EmailField()