from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, TourGuide, Student

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id','email', 'username',]

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(TourGuide)
admin.site.register(Student)