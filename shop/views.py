from django.shortcuts import render
from .models import *

def home(request):
    products =  Product.objects.all()
    context = {'products':products}
    return render (request,'shop/home.html',context)

def cart (request):
    context = {}
    return render (request,'shop/cart.html',context)

def checkout (request):
    if request.method=="POST":
       items_json = request.POST.get("itemsJson", "")
       name = request.POST.get("name", "")
       email = request.POST.get("email", "")
       address = request.POST.get("address", "")
       city = request.POST.get("city", "")
       state = request.POST.get("state", "")
       zip_code = request.POST.get("zip_code", "")
       phone = request.POST.get("phone", "")

       order = Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
       order.save()
       thank = True
       id = order.order_id
       return render(request,'shop/checkout.html', {'thank':thank, 'id':id})
    return render (request,'shop/checkout.html')

def prodview (request, myid):
    product = Product.objects.filter(id=myid)
    return render (request,'shop/prods.html',{'product':product[0]})
