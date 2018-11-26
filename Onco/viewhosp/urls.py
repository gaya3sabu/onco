from django.conf.urls import url
from .views import viewhosp

app_name = 'viewhosp'
urlpatterns = [
    url(r'^$', viewhosp, name='Form'),
    ]