from django.conf.urls import url
from .views import hospreg, edit_hospreg, delete_hospreg

app_name = 'hospital'
urlpatterns = [
    url(r'^$', hospreg, name='HospRegForm'),
    url(r'^edit_feedback/(?P<pk>\d+)/$', edit_hospreg, name='edit_hospreg'),
    url(r'^delete_feedback/(?P<pk>\d+)/$', delete_hospreg, name='delete_hospreg'),
]