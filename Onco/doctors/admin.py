from django.contrib import admin
from .models import Doctors


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ["name", "place", "city", "district", "email", "phone", "hosp_name"]


admin.site.register(Doctors, DoctorsAdmin)

# Register your models here.
