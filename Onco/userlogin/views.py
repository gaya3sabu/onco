from django.shortcuts import render, redirect
from . import forms
from user.models import User


def userhome(request):
    return render(request, 'userhomepage/userhomepage.html', {'logid': request.session['logid']})


def userlogin(request):
    if request.method == 'POST':

        form = forms.login_forms(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            if User.objects.filter(username=username).exists() and User.objects.filter(password=password).exists():
                obj = User.objects.get(username=username)

                request.session['logid'] = obj.id
                return redirect('userlogin:userhome')
            else:
                return render(request, 'userlogin/userlogin.html', {'form': form})
    else:
        form = forms.login_forms()
    return render(request, 'userlogin/userlogin.html', {'form': form})
