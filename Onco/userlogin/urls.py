
from django.conf.urls import url
from .views import userlogin, userhome


app_name = 'userlogin'

urlpatterns = [
    url(r'^$', userlogin, name='login_forms'),
    url(r'^userhome$', userhome, name='userhome'),

]
