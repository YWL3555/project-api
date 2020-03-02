from django.shortcuts import render
from rest_framework import viewsets
from .models import User, TourGuide, Student
from .serializers import TourGuideSerializer, StudentSerializer, UserSerializer, TripSerializer, TripDateSerializer, BookingSerializer, PrivateBookingSerializer, RatingReviewSerializer
from core.models import Trip, TripDate, Booking, PrivateBooking, RatingReview

from core import permissions
from .serializers import AcceptPrivateBookingSerializer


class AcceptPrivateBookingAPIView(generics.CreateAPIView):
    serializer_class = AcceptPrivateBookingSerializer
    permission_classes = (permissions.IsTourGuide,)

    def get_serializer_context(self):
        context = (
            super(AcceptPrivateBookingAPIView, self)
            .get_serializer_context()
        )
        context.update({
            'privateBookingId': self.kwargs.get('id'),
        })
        return context


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

class TripView(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripDateView(viewsets.ModelViewSet):
    queryset = TripDate.objects.all()
    serializer_class = TripDateSerializer

class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class PrivateBookingView(viewsets.ModelViewSet):
    queryset = PrivateBooking.objects.all()
    serializer_class = PrivateBookingSerializer

class RatingReviewView(viewsets.ModelViewSet):
    queryset = RatingReview.objects.all()
    serializer_class = RatingReviewSerializer