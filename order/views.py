import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from menu.models import Item, Category, Toppings
from .models import Cart, Order
from users.models import Profile, Address

def index(request):

    items = Item.objects.all()
    context = {
        'items':items
        }
    return render(request, "order/menu.html", context)


def menu(request, category_id):

    if category_id == 0:
        items = Item.objects.all()
    else:
        items = Item.objects.filter(category=category_id).all()
    context = {
        'items':items
        }
    return render(request, "order/menu.html",context)


def get_item(request, item_id):
    #fetch item details
    item = Item.objects.filter(id=item_id).first()
    context = {
        'item':item
        }
    return render(request,'order/item.html', context)


def add_item(request, item_id):
    if request.method == 'POST':
        #fetch item details
        v_item = Item.objects.filter(id=item_id).first()
        v_price = v_item.price 
        v_quantity = request.POST.get('quantity')
        v_total = float(v_price) * float(v_quantity)
        #create and save cart
        cart = Cart(item= v_item, quantity = v_quantity, item_name = v_item.item_name, total = v_total, price = v_price, user= request.user)
        cart.save()
    return redirect("show_cart")

def delete_item(request, item_id):
    #select and deelte item from the cart
    Cart.objects.get(id=item_id).delete()
    return redirect("show_cart")

def get_cart_details(request):
    #fetch details of items in cart
    cart_items =  Cart.objects.filter(status='Initiated', user=request.user).all()
    #calculate the total cost of cart items
    total = 0.0
    for item in cart_items:
        total += float(item.total)
    total = round(total,4)
    
    cart = {
        'cart_items':cart_items,
        'order_total': total
    }
    return cart 

def show_cart(request):
      
    context = get_cart_details(request)
    return render(request, 'order/cart.html', context)

def checkout(request):
    cart_items = get_cart_details(request)
    profile = Profile.objects.filter(user=request.user).first()
    try:
        address = profile.get_address_list()
    except:
        address= None

    cart_items.update({'address':address})
    context=cart_items

    return render(request, 'order/checkout.html',context)

def place_order(request):
    return redirect("index")