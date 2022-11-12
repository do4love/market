from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]