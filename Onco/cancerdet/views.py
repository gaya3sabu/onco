from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Cancerdet


def cancerdetreg(request):
    login_id = request.session['logid']
    model_object = Cancerdet.objects.filter(mgr_id=login_id)

    if request.method == "POST":
        form = forms.CandetRegForm(request.POST, request.FILES)
        if form.is_valid():
            detObj = form.cleaned_data
            name = detObj['name']
            symptom = detObj['symptom']
            cause = detObj['cause']
            test = detObj['test']
            treatment = detObj['treatment']
            a = Cancerdet(name=name, symptom=symptom, cause=cause, test=test, treatment=treatment, mgr_id=login_id)
            a.save()
            return redirect('cancerdet:CandetRegForm')
    else:
        form = forms.CandetRegForm

    return render(request, "cancerdet/cancerdet.html", {'form': form, 'data': model_object})


def edit_cancerdetreg(request, pk):
    login_id = request.session['logid']
    model_objects = Cancerdet.objects.filter(mgr_id=login_id)
    template = 'cancerdet/cancerdet.html'
    post = get_object_or_404(Cancerdet, pk=pk)

    if request.method == 'POST':
        form = forms.CandetRegForm(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('cancerdet:CandetRegForm')
    else:
        form = forms.CandetRegForm(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_objects,
        }
    return render(request, template, context)


def delete_cancerdetreg(request, pk):
    post = get_object_or_404(Cancerdet, pk=pk)
    post.delete()
    return redirect('cancerdet:CandetRegForm')
