from django.conf.urls import url
from .views import viewdoc

app_name = 'viewdoc'
urlpatterns = [
    url(r'^$', viewdoc, name='Form'),
    ]