from django.shortcuts import render
from django.http import HttpResponse

from .models import Product,Contact
from .models import Product,Officestationary,Desktopstationary,Artiststationary,Writtingstationary,Paper_and_pad,Filling_and_storage_stationary,Electronicstationary,Printing_material


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

    allprods = []
    catprods = Officestationary.objects.values('category', 'products_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old);
    print(list_new)
    for cat in list_new:
        prod = Officestationary.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    context = {'allprod': allprods}
    return render(request,'myShop/office.html',context)

def Desktop_stationary(request):
    allprods = []
    catprods = Desktopstationary.objects.values('category', 'products_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old);
    print(list_new)
    for cat in list_new:
        prod = Desktopstationary.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    context = {'allprod': allprods}
    return render(request,'myShop/Desktopstationary.html',context)

def Artist_stationary(request):
    allprods = []
    catprods = Artiststationary.objects.values('category', 'products_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old);
    print(list_new)
    for cat in list_new:
        prod = Artiststationary.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    context = {'allprod': allprods}
    return render(request,'myShop/Artiststationary.html',context)


def Writting_stationary(request):
    allprods = []
    catprods = Writtingstationary.objects.values('category', 'products_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old);
    print(list_new)
    for cat in list_new:
        prod = Writtingstationary.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    context = {'allprod': allprods}
    return render(request,'myShop/Writtingstationary.html',context)



def Paperandpad(request):
    allprods = []
    catprods =  Paper_and_pad.objects.values('category', 'products_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old);
    print(list_new)
    for cat in list_new:
        prod =  Paper_and_pad.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    context = {'allprod': allprods}
    return render(request,'myShop/Paper_and_pad.html',context)


def Fillingandstoragestationary(request):
    allprods = []
    catprods =  Filling_and_storage_stationary.objects.values('category', 'products_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old);
    print(list_new)
    for cat in list_new:
        prod =  Filling_and_storage_stationary.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    context = {'allprod': allprods}
    return render(request,'myShop/Filling_and_storage_stationary.html',context)    




def Electronic_stationary(request):
    allprods = []
    catprods =  Electronicstationary.objects.values('category', 'products_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old);
    print(list_new)
    for cat in list_new:
        prod =  Electronicstationary.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    context = {'allprod': allprods}
    return render(request,'myShop/Electronicstationary.html',context)    




def Printingmaterial(request):
    allprods = []
    catprods =  Printing_material.objects.values('category', 'products_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    list_old = list(cats)
    list_new = sorted(list_old);
    print(list_new)
    for cat in list_new:
        prod = Printing_material.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])

    context = {'allprod': allprods}
    return render(request,'myShop/Printing_material.html',context)    





def checkout(request):
    return render(request,"myShop/checkout.html")
def term(request):
    return render(request,"myShop/term.html")
def villageContact(request):
    return render(request,"myShop/VillagePro.html")