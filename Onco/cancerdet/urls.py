from django.conf.urls import url
from .views import cancerdetreg, edit_cancerdetreg, delete_cancerdetreg

app_name = 'cancerdet'
urlpatterns = [
    url(r'^$', cancerdetreg, name='CandetRegForm'),
    url(r'^edit_cancerdetreg/(?P<pk>\d+)/$', edit_cancerdetreg, name='edit_cancerdetreg'),
    url(r'^delete_cancerdetreg/(?P<pk>\d+)/$', delete_cancerdetreg, name='delete_cancerdetreg'),
]
