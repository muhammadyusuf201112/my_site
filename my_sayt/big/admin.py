from django.contrib import admin

from .models import User

# Register your models here.


@admin.register(User)
class Users(admin.ModelAdmin):
    model = User
    list_display = ['frist_name', 'last_name', 'work']