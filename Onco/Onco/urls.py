"""Onco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^userreg/', include('user.urls')),
    url(r'^userlogin/', include('userlogin.urls')),
    url(r'^parlourreg/', include('parlour.urls')),
    url(r'^bduserreg/', include('bduser.urls')),
    url(r'^parlourlogin/', include('parlourlogin.urls')),
    url(r'^bduserlogin/', include('bduserlogin.urls')),
    url(r'^hospreg/', include('hospital.urls')),
    url(r'^docreg/', include('doctors.urls')),
    url(r'^managerlogin/', include('managerlogin.urls')),
    url(r'^cancerdetreg/', include('cancerdet.urls')),
    url(r'^viewcan/', include('cancerview.urls')),
    url(r'^viewhosp/', include('viewhosp.urls')),
    url(r'^viewdoc/', include('viewdoc.urls')),

    # url(r'^$', include('mainhome.urls')),


]

