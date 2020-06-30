from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Product, Orders, Contact, Request
from math import ceil

# Create your views here.
def index(request):
    allprods = []

    catprods = Product.objects.values('category', 'product_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    mats_pro = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old)
    lis_old = list(cats)
    lis_new = sorted(list_old)
    print(list_new)
    for cat in list_new:
        prod = Product.objects.filter(category=cat)
        print(prod)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    param = {'allprod': allprods}
    print(param)
    return render(request,'myShop/Home.html',param)

def about(request):
    return render(request,'myShop/about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thanks = True
        return render(request,'myShop/contact.html',{'thanks':thanks})
    return render(request,'myShop/contact.html')


def tracker(request):
    return HttpResponse("tracker")
def search(request):
    return HttpResponse("Search")
def viewproduct(request,product_id):
    print(product_id)
    product = Product.objects.filter(product_id=product_id)[0]
    print(product)
    return render(request, 'myShop/productView.html', {'prod': product})



def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        zip_code = request.POST.get('zip_code', '')
        order = Orders(items_json=items_json,name=name,email=email,amount=amount,address=address,city=city,state=state,phone=phone,zip_code=zip_code)
        order.save()
        thank = True;
        id = order.order_id;
        return render(request, 'myShop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'myShop/checkout.html')


def term(request):
    return render(request,"myShop/term.html")
# this is for storing product request
def villageContact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        image = request.POST.get('image','')
        request_post = Request(name = name, email = email, phone = phone, desc = desc, image = image)
        print(request_post)
        request_post.save()
        thanks = True
        return render(request,'myShop/VillagePro.html',{'thanks':thanks})
    return render(request,"myShop/VillagePro.html")