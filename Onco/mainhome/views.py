from django.shortcuts import render, redirect


def mainhome(request):
    return render(request, 'mainhome/mainhome.html', {})


