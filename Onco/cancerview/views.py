from django.shortcuts import render, redirect
from cancerdet.models import Cancerdet

def viewcan(request):
    model_object = Cancerdet.objects.all()
    return render(request, "viewcancerdet/viewcancerdet.html", {'data': model_object})
