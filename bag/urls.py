from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<slug:slug>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<slug:slug>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<slug:slug>/', views.remove_from_bag, name='remove_from_bag'),
]
