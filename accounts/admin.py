from django.contrib import admin
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display =('name','phone','email','date_created')

admin.site.register(Customer,CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price','category','date_created')

admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
	list_display = ('customer','product','date_created')

admin.site.register(Order,OrderAdmin)

admin.site.register(Tag)