from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from decimal import Decimal

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
    gender = models.CharField(max_length=8)
    contactNumber = models.CharField(max_length=15)
    profilePic = models.ImageField(upload_to='photos')

class TourGuide(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    email = models.EmailField()
    gender = models.CharField(max_length=8)
    contactNumber = models.CharField(max_length=15)
    profilePic = models.ImageField(upload_to='photos')
    languages = ArrayField(models.CharField(max_length=20, blank=True))
    tourGuideType = models.CharField(max_length=10)
    averageRating = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal(0))
    totalRating = models.IntegerField()

class Trip(models.Model):
    title = models.CharField(max_length=70)
    city = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    duration = models.IntegerField()
    size = models.IntegerField()
    TourGuide = models.ForeignKey(TourGuide, on_delete=models.CASCADE)
    languages = ArrayField(models.CharField(max_length=20, blank=True))
    description = models.TextField(max_length=4000)
    photo = models.ImageField(upload_to='photos')
    averageRating = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal(0))
    totalRating = models.IntegerField()

class TripDate(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    availablePax = models.IntegerField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    
class Booking(models.Model):
    tripDate = models.ForeignKey(TripDate,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    pax = models.IntegerField()
    reviewed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)

class PrivateBooking(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    details = models.TextField()
    city = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    pax = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tourGuide = models.ForeignKey(TourGuide, on_delete=models.CASCADE)
    reviewed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)

class RatingReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    tourGuide = models.ForeignKey(TourGuide, on_delete=models.CASCADE)