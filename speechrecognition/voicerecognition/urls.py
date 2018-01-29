from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.file_upload, name="file_upload"),
    url(r'^final$', views.file_upload_final, name="file_upload_final")    
]
