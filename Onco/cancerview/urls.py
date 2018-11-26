from django.conf.urls import url
from .views import viewcan

app_name = 'cancerview'
urlpatterns = [
    url(r'^$', viewcan, name='Form'),
    ]