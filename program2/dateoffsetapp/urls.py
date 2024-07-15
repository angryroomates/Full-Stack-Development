from django.urls import path
from . import views

urlpatterns = [
    path('',views.dateoffset, name = 'home' ),
    path('<int:offset>', views.dateoffsetnum, name = 'custom_num'),
]