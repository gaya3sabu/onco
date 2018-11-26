from django.contrib import admin
from .models import Hospital


class HospitalAdmin(admin.ModelAdmin):
    list_display = ["name", "place", "city", "district", "email", "phone"]


admin.site.register(Hospital, HospitalAdmin)