from django.urls import path
from . import views

urlpatterns = [
    path('', views.datetimeview, name='home'),
    path('date/', views.dateview, name='date'),
    path('time/', views.timeview, name='time'),
]
