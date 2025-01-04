from django.shortcuts import render
from .models import Product, Category


def all_products(request):
    return render(request, 'products/all_products.html')