from django.shortcuts import render
from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('projects', views.projects_page_view, name='projects'),
    path('licenciatura', views.uni_page_view, name='licenciatura'),
    path('contact', views.contact_page_view, name='contact')
]