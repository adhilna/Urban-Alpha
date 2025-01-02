from django.contrib import admin
from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'created', 'updated', 'in_stock']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['in_stock', 'price']
    prepopulated_fields = {'slug': ('name',)}