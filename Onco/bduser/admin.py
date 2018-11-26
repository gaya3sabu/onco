from django.contrib import admin
from .models import Bduser


class BduserAdmin(admin.ModelAdmin):
    list_display = ["name", "place", "gender", "age", "city", "district", "email", 'bloodgroup', "phone", "username", "password"]


admin.site.register(Bduser, BduserAdmin)
