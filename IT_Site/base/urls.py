from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('all_courses', views.all_courses, name="all_courses"),
    path('course/<str:pk>/', views.course, name="course"),
]