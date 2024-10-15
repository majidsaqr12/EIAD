from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),       
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('register/<int:course_id>/', views.register_course, name='register_course'),
]
