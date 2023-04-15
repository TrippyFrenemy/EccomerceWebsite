from django.contrib import admin
from .models import Category, Product, Orders, Cart, CartItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Cart)
admin.site.register(CartItem)

