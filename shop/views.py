from django.shortcuts import render
from .models import *
import json
import io
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string


def home(request):
    products =  Product.objects.all()
    context = {'products':products}
    return render (request,'shop/home.html',context)

def cart (request):
    context = {}
    return render (request,'shop/cart.html',context)

def checkout (request):
    if request.method=="POST":
       data = json.loads(request.POST.get("itemsJson", ""))
       items_json = data 
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


def myorders(request):
    if 'search' in request.GET:
        search = request.GET['search']
        myorder = Order.objects.filter(date__icontains=search)
    else:    
        myorder = Order.objects.all()
    context = {'myorder':myorder}
    return render (request,'shop/history.html',context)



def product_api(request):
    if request.method =='GET':
        json_data = request.body 
        prod = Product.objects.all()
        serializer = ProductSerializer(prod, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
