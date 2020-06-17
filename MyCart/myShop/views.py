from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
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
    return HttpResponse("Hello")
def contact(request):
    return HttpResponse("contact")
def tracker(request):
    return HttpResponse("tracker")
def search(request):
    return HttpResponse("Search")
def viewproduct(request):
    return HttpResponse("viewproduct")
def checkout(request):
    return HttpResponse("checkout")