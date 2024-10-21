from django.urls import path
from . import views

urlpatterns = [
    path('', views.program, name='programs'),
]
