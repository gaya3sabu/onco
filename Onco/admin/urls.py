from django.conf.urls import url
from .views import login,adminhome

app_name = 'Login'

urlpatterns = [
    url(r'^$', login, name='Login_Forms'),
    url(r'^adminhome$', adminhome, name='adminhome'),


]