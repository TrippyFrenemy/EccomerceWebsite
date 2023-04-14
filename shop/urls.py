from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:category_slug>", views.home, name="products_by_category"),
    path("category/<slug:category_slug>/<slug:product_slug>", views.product, name="product_detail"),
    path("about/", views.about, name="about"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>", views.add_cart, name="add_cart"),
    path("cart/remove/<int:product_id>", views.cart_remove, name="cart_remove"),
    path("cart/delete/<int:product_id>", views.cart_delete, name="cart_delete"),
    path("order", views.order, name="order"),
    path("account/create", views.sign_up, name="sign_up"),
    path("account/login", views.login_view, name="login"),
    path("account/logout", views.logout_view, name="logout"),
]
