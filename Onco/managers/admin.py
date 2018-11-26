from django.contrib import admin
from .models import Managers


class ManagersAdmin(admin.ModelAdmin):
    list_display = ["mgr_name", "mgr_place", "mgr_gender", "mgr_age", "mgr_city", "mgr_district", "mgr_email", "mgr_phone", "mgr_username", "mgr_password"]


admin.site.register(Managers, ManagersAdmin)
