from django.conf.urls import url
from .views import  docreg, edit_docreg, delete_docreg


app_name = 'doctors'
urlpatterns = [
    url(r'^$', docreg, name='DocRegForm'),
    url(r'^edit_feedback/(?P<pk>\d+)/$', edit_docreg, name='edit_docreg'),
    url(r'^delete_feedback/(?P<pk>\d+)/$', delete_docreg, name='delete_docreg'),
]