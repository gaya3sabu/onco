from django.conf.urls import url
from .views import fstpage

app_name = 'fstpage'

urlpatterns = [
    url(r'^$', fstpage, name='fstpage'),

]
