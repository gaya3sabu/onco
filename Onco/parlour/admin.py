from django.contrib import admin
from .models import Parlour


class ParlourAdmin(admin.ModelAdmin):
    list_display = ["parlour_id", "name", "place", "city", "district", "email", "phone"]


admin.site.register(Parlour, ParlourAdmin)



