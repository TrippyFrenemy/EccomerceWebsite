from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Create your views here.
def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug= category_slug)
        products = Product.objects.filter(category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    dict = {
        "category": category_page,
        "products": products
    }
    return render(request, "home.html", dict)


def about(request):
    return render(request, "about.html")


def product(request, category_slug=None, product_slug=None):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    dict={
        "product": product
    }
    return render(request, "product.html", dict)
