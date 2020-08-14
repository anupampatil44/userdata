from django.urls import path
from . import views
from django.urls import re_path
urlpatterns = [
    path('', views.register, name='register'),
    path('search/',views.search,name='search'),
]