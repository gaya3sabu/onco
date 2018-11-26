from django.conf.urls import url
from .views import mainhome

app_name = 'mainhome'

urlpatterns = [
    url(r'^$', mainhome, name='mainhome'),

]
