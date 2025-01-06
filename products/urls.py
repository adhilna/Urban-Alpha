from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='home'),
    path('product_store/', views.product_store, name='store'),
    path('item/<slug:slug>/', views.product_detail, name='item')
]