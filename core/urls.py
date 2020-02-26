from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tour-guides', views.tourGuideView)

urlpatterns = [
    path('', include(router.urls))
]