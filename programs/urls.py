from django.urls import path
from . import views

urlpatterns = [
    path('', views.program, name='programs'),
    path('register/<int:program_id>/', views.register_program, name='register_program'),
]
