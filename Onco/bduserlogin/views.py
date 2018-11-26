from django.shortcuts import render,redirect
from . import forms
from bduser.models import Bduser


def bduserhome(request):
    return render(request, 'userhomepage/userhomepage.html', {'logid': request.session['logid']})


def bduserlogin(request):
    if request.method =='POST':

        form = forms.login_forms(request.POST)
        if form.is_valid():
            bduserObj = form.cleaned_data
            username = bduserObj['username']
            password = bduserObj['password']
            if Bduser.objects.filter(username=username).exists() and Bduser.objects.filter(password=password).exists():
                obj = Bduser.objects.get(username=username)

                request.session['logid'] = obj.id
                return redirect('bduserlogin:bduserhome')
            else:
                return render(request, 'bduserlogin/bduserlogin.html', {'form': form})
    else:
        form = forms.login_forms()
    return render(request, 'bduserlogin/bduserlogin.html', {'form': form})
