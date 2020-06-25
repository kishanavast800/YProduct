# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='StartHome'),
    path('about/',views.about,name='aboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='trackerStatus'),
    path('search/',views.search,name='Search'),
    path('viewproduct/',views.viewproduct,name='ViewProduct'),

    path('showCart/', views.showCart, name='showCart'),
    path('Desktopstationary/',views.Desktop_stationary,name='Desktop_stationary'),
    path('Artiststationary/',views.Artist_stationary,name='Artist_stationary'),
    path('Writtingstationary/',views.Writting_stationary,name='Writting_stationary'),
    path('Paper_and_pad/',views.Paperandpad,name='Paperandpad'),
    path('Filling_and_storage_stationary/',views.Fillingandstoragestationary,name='Fillingandstoragestationary'),
    path('Electronicstationary/',views.Electronic_stationary,name='Electronic_stationary'),
    path('Printing_material/',views.Printingmaterial,name='Printingmaterial'),
    path('checkout/',views.checkout,name='checkout'),
    path('term/', views.term, name='term'),
    path('villageContact/', views.villageContact, name='villageContact'),


]
