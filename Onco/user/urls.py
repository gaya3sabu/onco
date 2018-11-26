from django.conf.urls import url
from .views import userreg


app_name = 'user'
urlpatterns = [
    url(r'^$', userreg, name='UserRegForm')
]