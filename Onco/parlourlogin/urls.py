from django.conf.urls import url
from .views import parlourlogin, parlourhome


app_name = 'parlourlogin'

urlpatterns = [
    url(r'^$', parlourlogin, name='login_forms'),
    url(r'^parlourhome$', parlourhome, name='parlourhome'),

]