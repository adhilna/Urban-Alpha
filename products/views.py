from django.shortcuts import render
from .models import Product, Category


def all_products(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {'products': products, 'category': category}
    return render(request, 'products/products.html', context=context)
