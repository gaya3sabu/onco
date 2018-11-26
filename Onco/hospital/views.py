from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Hospital


def hospreg(request):
    login_id = request.session['logid']
    model_object = Hospital.objects.filter(mgr_id=login_id)

    if request.method == "POST":
        form = forms.HospRegForm(request.POST, request.FILES)
        if form.is_valid():
            hosObj = form.cleaned_data
            name = hosObj['name']
            place = hosObj['place']
            city = hosObj['city']
            district = hosObj['district']
            email = hosObj['email']
            phone = hosObj['phone']
            a = Hospital(name=name, place=place, city=city, district=district, email=email, phone=phone,
                         mgr_id=login_id)
            a.save()
            return redirect('hospital:HospRegForm')
    else:
        form = forms.HospRegForm

    return render(request, "hospital/hospital.html", {'form': form, 'data': model_object})


def edit_hospreg(request, pk):
    login_id = request.session['logid']
    model_objects = Hospital.objects.filter(mgr_id=login_id)
    template = 'hospital/hospital.html'
    post = get_object_or_404(Hospital, pk=pk)

    if request.method == 'POST':
        form = forms.HospRegForm(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('hospital:HospRegForm')
    else:
        form = forms.HospRegForm(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_objects,
        }
    return render(request, template, context)


def delete_hospreg(request, pk):
    post = get_object_or_404(Hospital, pk=pk)
    post.delete()
    return redirect('hospital:HospRegForm')


