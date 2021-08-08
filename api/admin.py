from django.contrib import admin
from .models import UserApiModel

# Register your models here.
@admin.register(UserApiModel)
class UserApiModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age', 'dob', 'mobile_no')
