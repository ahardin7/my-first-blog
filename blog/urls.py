from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_me', views.about_me, name='about_me'),
    path('proj_list', views.proj_list, name='proj_list'),
]