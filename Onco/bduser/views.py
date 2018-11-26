from django.shortcuts import render, redirect
from .import forms


def bduserreg(request):
    if request.method =='POST':
        form = forms.BduserRegForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('bduser:BduserRegForm')
    else:
        form = forms.BduserRegForm

    return render(request, "bduserreg/bduserregs.html", {'form': form})

