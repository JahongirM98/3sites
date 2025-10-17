from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request):
    categories = Category.objects.all().order_by("name")
    products = Product.objects.select_related("category").all().order_by("name")
    return render(request, "catalog/product_list.html", {"categories": categories, "products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "catalog/product_detail.html", {"product": product})
