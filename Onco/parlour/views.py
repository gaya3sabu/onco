from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Parlour


def parlourreg(request):
    login_id = request.session['logid']
    model_object = Parlour.objects.filter(mgr_id=login_id)

    if request.method == "POST":
        form = forms.ParlourRegForm(request.POST, request.FILES)
        if form.is_valid():
            parObj = form.cleaned_data
            parlour_id = parObj['parlour_id']
            name = parObj['name']
            place = parObj['place']
            city = parObj['city']
            district = parObj['district']
            email = parObj['email']
            phone = parObj['phone']
            a = Parlour(parlour_id=parlour_id, name=name, place=place, city=city, district=district, email=email,
                        phone=phone, mgr_id=login_id)
            a.save()
            return redirect('parlour:ParlourRegForm')
    else:
        form = forms.ParlourRegForm

    return render(request, "parlour/parlourhome.html", {'form': form, 'data': model_object})


def edit_parlourreg(request, pk):
    login_id = request.session['logid']
    model_objects = Parlour.objects.filter(mgr_id=login_id)
    template = 'parlour/parlourhome.html'
    post = get_object_or_404(Parlour, pk=pk)

    if request.method == 'POST':
        form = forms.ParlourRegForm(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('parlour:ParlourRegForm')
    else:
        form = forms.ParlourRegForm(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_objects,
        }
    return render(request, template, context)


def delete_parlourreg(request, pk):
    post = get_object_or_404(Parlour, pk=pk)
    post.delete()
    return redirect('parlour:ParlourRegForm')


