from rest_framework import serializers
from .models import TourGuide, Student, User
from django.db import IntegrityError, transaction
from djoser.conf import settings

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'name', 'email', 'is_student', 'is_tourGuide', 'password')

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
        fields = ('user_id', 'name')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user_id', 'name')

