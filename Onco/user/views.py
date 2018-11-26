from django.shortcuts import render, redirect
from .import forms


def userreg(request):
    if request.method =='POST':
        form = forms.UserRegForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('user:UserRegForm')
    else:
        form = forms.UserRegForm

    return render(request, "userreg/registration.html", {'form': form})







