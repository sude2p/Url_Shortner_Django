from django.urls import path 
from .views import *

urlpatterns = [
    
    path('url/',urlView, name='url'),
    path('<str:shorturl>/',redirecturl, name='redirecturl'),
    
   
]
