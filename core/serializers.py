from rest_framework import serializers
from .models import tourGuide

class tourGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = tourGuide
        fields = ('id', 'name', 'description', 'email')