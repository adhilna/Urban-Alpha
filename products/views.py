from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def all_products(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {'products': products, 'category': category}
    return render(request, 'products/products.html', context=context)


def product_store(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {'products': products, 'category': category}
    return render(request, 'products/store.html', context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    category = Category.objects.all()
    context = {'product': product, 'category': category}
    return render(request, 'products/detail.html', context=context)