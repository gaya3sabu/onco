from django.contrib import admin
from .models import Charity


class CharityAdmin(admin.ModelAdmin):
    list_display = ["charitytype"]


admin.site.register(Charity, CharityAdmin)