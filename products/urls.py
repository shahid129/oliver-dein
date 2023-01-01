from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit/<slug:slug>/', views.edit_product, name='edit_product'),

]
