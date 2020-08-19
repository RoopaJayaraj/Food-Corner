
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("menu/<int:category_id>", views.menu, name="menu"),
    path("get_item/<int:item_id>", views.get_item, name="get_item"),
    path("add_item/<int:item_id>", views.add_item, name="add_item"),
    path("delete/<int:item_id>", views.delete_item, name="delete"),
    path("show_cart/", views.show_cart, name="show_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("placeOrder/", views.place_order, name="placeOrder"),
]
