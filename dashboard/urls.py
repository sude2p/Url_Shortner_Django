from django.urls import path 
from .views import *

urlpatterns = [
    path('dashboard/',dashBoard, name='dashboard'),
    path('delete/<int:pk>/', urlDelete, name='url-delete'),

    
   
]
