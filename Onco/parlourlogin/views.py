from django.shortcuts import render, redirect
from . import forms
from parlour.models import Parlour


def parlourhome(request):
    return render(request, 'parlourhomepage/parlourhomepage.html', {'logid': request.session['logid']})


def parlourlogin(request):
    if request.method =='POST':

        form = forms.login_forms(request.POST)
        if form.is_valid():
            parlourObj = form.cleaned_data
            username = parlourObj['username']
            password = parlourObj['password']
            if Parlour.objects.filter(username=username).exists() and Parlour.objects.filter(password=password).exists():
                obj = Parlour.objects.get(username=username)

                request.session['logid'] = obj.id
                return redirect('parlourlogin:parlourhome')
            else:
                return render(request, 'parlourlogin/parlourlogin.html', {'form': form})
    else:
        form = forms.login_forms()
    return render(request, 'parlourlogin/parlourlogin.html', {'form': form})
