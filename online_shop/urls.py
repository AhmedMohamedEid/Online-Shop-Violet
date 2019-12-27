from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:id>", views.subcategoies, name="subcategoies"),
    path("product/<int:id>", views.product_page, name="product"),
    path("shopping_cart", views.shopping_cart, name="shopping_cart"),
    path("add2chart", views.add2chart, name="add2chart"),
    path("clear_cart", views.clear_cart, name="clear_cart"),
    path("delete_order", views.delete_order, name="delete_order"),
    path("calc_total", views.calc_total, name="calc_total"),
    path("checkout", views.checkout, name="checkout"),
    path("contact", views.contact_us, name="contact"),

]
