from django.conf.urls import url
from .views import  bduserreg


app_name = 'bduser'
urlpatterns = [
    url(r'^$', bduserreg, name='BduserRegForm')
]
