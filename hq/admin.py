from django.contrib import admin

from .models import Product, ProductOrder, Order, User, CargoPrice

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductOrder)
admin.site.register(User)
admin.site.register(CargoPrice)
