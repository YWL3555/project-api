from django.shortcuts import render
from rest_framework import viewsets
from .models import User, TourGuide, Student
from .serializers import TourGuideSerializer, StudentSerializer, UserSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TourGuideView(viewsets.ModelViewSet):
    queryset = TourGuide.objects.all()
    serializer_class = TourGuideSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer