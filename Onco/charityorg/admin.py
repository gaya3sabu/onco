from django.contrib import admin
from .models import Charityorg


class CharityorgAdmin(admin.ModelAdmin):
    list_display = ["name", "place", "city", "district", "email", "phone", "charitytype", "username", "password"]


admin.site.register(Charityorg, CharityorgAdmin)

# Register your models here.
