from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),       
    path('about/', views.about, name='about'),    
    path('contact/', views.contact, name='contact'),  
    path('our_campus/', views.our_campus, name='our_campus'),
    path('success/', views.success, name='success'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
