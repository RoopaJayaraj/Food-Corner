from django.shortcuts import render
from menu.models import Item, Category, Toppings


def index(request):
    item = Item.objects.all()
    context={'items':item}
    
    return render(request, "order/menu.html", context)

def layout(request):
    return render(request, 'order/layout.html')
