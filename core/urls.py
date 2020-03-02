from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tour-guides', views.TourGuideView)
router.register('students', views.StudentView)
router.register('users', views.UserView)
router.register('bookings', views.BookingView)
router.register('private-bookings', views.PrivateBookingView)
router.register('trips', views.TripView)
router.register('trip-dates', views.TripDateView)
router.register('rating-reviews', views.RatingReviewView)

urlpatterns = [
    path('', include(router.urls))
]