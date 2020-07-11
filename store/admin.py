from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
from .models import Order

class AdminProduct(admin.ModelAdmin):
	list_display = ['id', 'name','price','category', 'date']


class AdminCategory(admin.ModelAdmin):
	list_display = ['name']



admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
