from django.contrib import admin
from .models import Category, Toppings, Item
# Register your models here.
admin.site.register(Category)
admin.site.register(Toppings)
admin.site.register(Item)
