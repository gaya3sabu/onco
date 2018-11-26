from django.shortcuts import render, redirect


def fstpage(request):
    return render(request, 'fstpage/fstpage.html', {})


