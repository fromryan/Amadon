from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def buying_process(request,id):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
   
    print("Charging credit card...")
    

    return redirect('/checkout')


def checkout(request,id):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    context = {
        'new_order': Order.objects.get(id=id),
    }
    return render(request,"store/checkout.html", context)