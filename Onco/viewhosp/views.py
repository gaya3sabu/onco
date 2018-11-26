from django.shortcuts import render, redirect
from hospital.models import Hospital


def viewhosp(request):
    model_object = Hospital.objects.all()
    return render(request, "viewhosp/viewhosp.html", {'data': model_object})




