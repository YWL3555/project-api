from rest_framework import serializers, generics
from .models import TourGuide, Student, User
from django.db import IntegrityError, transaction
from djoser.conf import settings

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from core.models import Booking, Trip, TripDate, PrivateBooking, RatingReview
from rest_framework.generics import get_object_or_404
from django.contrib.auth import authenticate

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'name', 'email', 'is_student', 'is_tourGuide', 'password', 'tourGuideType')

    def createRole(self, user, validated_data):
        if validated_data['is_student']:
            student = Student.objects.create(user=user)
            return student
        
        if validated_data['is_tourGuide']:
            tourGuide = TourGuide.objects.create(user=user)
            return tourGuide
        
        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            self.createRole(user, validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TourGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourGuide
        fields = ('user_id', 'name', 'description', 'email', 'gender', 'contactNumber', 'profilePic', 'languages', 'tourGuideType', 'averageRating', 'totalRating')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user_id', 'name', 'email', 'gender', 'contactNumber', 'profilePic')
        
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('title', 'city', 'category', 'duration', 'size', 'tourGuide','languages','description','photo','averageRating','totalRating')

class TripDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripDate
        fields = ('startDate','endDate','availablePax','trip')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('tripDate','student','pax','reviewed','cancelled')

class PrivateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateBooking
        fields = ('startDate','endDate','details','city','status','pax','student','tourGuide','reviewed','cancelled')

class RatingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingReview
        fields = ('student','rating','review','trip','tourGuide')

# class AcceptPrivateBookingSerializer(serializers.ModelSerializer):
#     """Accept private booking serializer"""
#     class Meta:
#         model = PrivateBooking

#     @transaction.atomic
#     def create(self, validated_data):
#         privateBookingId = self.context.get('privateBookingId')
#         acceptedBooking = get_object_or_404(PrivateBooking, id=privateBookingId)
#         acceptedBooking.status = "Accepted"
#         return acceptedBooking.save()

