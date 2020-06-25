from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil
# Create your views here.
def index(request):
    allprods = []
    catprods = Product.objects.values('category', 'product_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old);

    for cat in list_new:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    param = {'allprod': allprods}
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
def viewproduct(request):
    return HttpResponse("viewproduct")
def showCart(request):
    return render(request,"myShop/cart.html")
def checkout(request):
    return render(request,"myShop/checkout.html")
def term(request):
    return render(request,"myShop/term.html")
def villageContact(request):
    return render(request,"myShop/VillagePro.html")