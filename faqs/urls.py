from django.urls import path
from . import views

urlpatterns = [
    path('', views.faqs, name='faqs'),
    path('add_faqs/', views.add_faqs, name='add_faqs'),
]