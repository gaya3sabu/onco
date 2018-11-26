from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "place", "gender", "age", "city", "district", "email", "phone", "username", "password"]


admin.site.register(User, UserAdmin)

# Register your models here.
