from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate
from django.apps import apps



def adminhome(request):
    return render(request, 'Admin/AdminHome.html', {'logid': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.Login_Forms(request.POST, request.FILES)
        if form.is_valid():
            userobj = form.cleaned_data
            username = userobj['username']
            password = userobj['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['logid'] = user.id
                request.session['logname'] = user.username
                return redirect('Login:adminhome')
            else:
                return render(request, 'Login.html', {'form': form})
               # if Centers.objects.filter(center_username=username).exists() and Centers.objects.filter(center_password=password).exists():
                  #  obj = Centers.objects.get(center_username=username)
                   # request.session['logid'] = obj.id
                    #request.session['logname'] = username
                    #return redirect('Login:centerhome')


        else:
            form = forms.Login_Forms()
            return render(request, 'Login.html', {'form': form})
    else:
        form = forms.Login_Forms()
        return render(request, 'Login.html', {'form': form})

# Create your views here.
