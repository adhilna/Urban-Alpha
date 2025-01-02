from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
