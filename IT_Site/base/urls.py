from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('all_courses', views.all_courses, name="all_courses"),
    path('course/<str:pk>/', views.course, name="course"),
    path('module/<str:pk>/', views.module, name="module"),
    path('faq', views.faq, name="faq"),
]