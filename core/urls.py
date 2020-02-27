from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tour-guides', views.TourGuideView)
router.register('students', views.StudentView)
router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls))
]