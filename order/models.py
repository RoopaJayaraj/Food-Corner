from django.db import models
from django.contrib.auth.models import User
from menu.models import Item

class Cart(models.Model):
    INITIATED = "Initiated"
    ORDERED = "Ordered"
    STATUS_CHOICES = (
        (INITIATED, "Initiated"),
        (ORDERED, "Ordered")
    )   
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, primary_key=False)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name= models.CharField(max_length=50, default='-')
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    status = status = models.CharField(max_length=10, choices=STATUS_CHOICES, default= INITIATED)

    def get_cart_item(self):
        return self.item_name

class Order(models.Model):
    STATUS_CHOICES = (
        ("INITIATED", "Initiated"),
        ( "PROGRESS", "Progress"),
        ("DELIVERED", "Deliverd")
    )    
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated= models.DateTimeField(auto_now_add=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, )
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    ref_code = models.IntegerField(null=True)
    cart = models.ManyToManyField(Cart)

    def get_cart_items(self):
        return self.cart.all()


    def get_cart_total(self):
        total=0
        for item in self.cart.all():
            total=total+item.total
        return total

