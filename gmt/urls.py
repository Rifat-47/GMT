# gmt/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.gmt_view, name='gmt'),
]
