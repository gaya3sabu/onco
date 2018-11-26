from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Doctors


def docreg(request):
    login_id = request.session['logid']
    model_object = Doctors.objects.filter(mgr_id=login_id)

    if request.method == "POST":
        form = forms.DocRegForm(request.POST, request.FILES)
        if form.is_valid():
            docObj = form.cleaned_data
            name = docObj['name']
            place = docObj['place']
            city = docObj['city']
            district = docObj['district']
            email = docObj['email']
            phone = docObj['phone']
            hosp_name = docObj['hosp_name']
            a = Doctors(name=name, place=place, city=city, district=district, email=email, phone=phone,
                        hosp_name=hosp_name, mgr_id=login_id)
            a.save()
            return redirect('doctors:DocRegForm')
    else:
        form = forms.DocRegForm

    return render(request, "doctor/doctor.html", {'form': form, 'data': model_object})


def edit_docreg(request, pk):
    login_id = request.session['logid']
    model_objects = Doctors.objects.filter(mgr_id=login_id)
    template = 'doctor/doctor.html'
    post = get_object_or_404(Doctors, pk=pk)

    if request.method == 'POST':
        form = forms.DocRegForm(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('doctors:DocRegForm')
    else:
        form = forms.DocRegForm(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_objects,
        }
    return render(request, template, context)


def delete_docreg(request, pk):
    post = get_object_or_404(Doctors, pk=pk)
    post.delete()
    return redirect('doctors:DocRegForm')







