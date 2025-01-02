from django.shortcuts import render
from .models import *


def all_products(request):
    products = Product.objects.all()
    parent_categories = Category.objects.filter(parent__isnull=True)
    context = {'products': products, 'parent_categories': parent_categories}
    return render(request, 'product/home.html', context)


