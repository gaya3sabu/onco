from django.conf.urls import url
from .views import parlourreg, edit_parlourreg, delete_parlourreg


app_name = 'parlour'
urlpatterns = [
    url(r'^$', parlourreg, name='ParlourRegForm'),
    url(r'^edit_feedback/(?P<pk>\d+)/$', edit_parlourreg, name='edit_parlourreg'),
    url(r'^delete_feedback/(?P<pk>\d+)/$', delete_parlourreg, name='delete_parlourreg'),
]