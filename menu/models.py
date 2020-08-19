from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Toppings(models.Model):
    topping_name = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, default=0.00)


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, default=0.00)
    availability = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    item_img = models.ImageField(upload_to = 'images/', blank=True)
