from django.conf.urls import url
from .views import bduserlogin, bduserhome


app_name = 'bduserlogin'

urlpatterns = [
    url(r'^$', bduserlogin, name='login_forms'),
    url(r'^bduserhome$', bduserhome, name='bduserhome'),

]
