from django.contrib import admin
from .models import Cancerdet




class CancerdetAdmin(admin.ModelAdmin):
    list_display = ["name", "symptom", "cause", "test", "treatment"]


admin.site.register(Cancerdet, CancerdetAdmin)
