from django.contrib import admin

# Register your models here.
from .models import Product,Officestationary,Desktopstationary,Artiststationary,Writtingstationary,Paper_and_pad,Filling_and_storage_stationary,Electronicstationary,Printing_material

admin.site.register(Product),
admin.site.register(Officestationary),
admin.site.register(Desktopstationary),
admin.site.register(Artiststationary),
admin.site.register(Writtingstationary),
admin.site.register(Paper_and_pad),
admin.site.register(Filling_and_storage_stationary),
admin.site.register(Electronicstationary),
admin.site.register(Printing_material)

