from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^maddy$', views.index, name="index"),
    url(r'^maddy/save$', views.save, name="save")    
]

