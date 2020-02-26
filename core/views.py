from django.shortcuts import render
from rest_framework import viewsets
from .models import tourGuide
from .serializers import tourGuideSerializer

# Create your views here.

class tourGuideView(viewsets.ModelViewSet):
    queryset = tourGuide.objects.all()
    serializer_class = tourGuideSerializer