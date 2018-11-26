from django.shortcuts import render, redirect
from doctors.models import Doctors

def viewdoc(request):
    model_object = Doctors.objects.all()
    return render(request, "viewdoc/viewdoc.html", {'data': model_object})
