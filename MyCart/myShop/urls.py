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
    path('checkout/',views.checkout,name='checkout'),

]
