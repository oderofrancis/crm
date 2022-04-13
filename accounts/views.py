from django.shortcuts import render
from .models import *

# Create your views here.

def dashboard(request):
	customers = Customer.objects.all()
	orders = Order.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'customers':customers,'orders':orders,
				'total_customers':total_customers,
				'total_orders':total_orders,
				'delivered':delivered,'pending':pending}

	return render(request,'accounts/dashboard.html',context)

def product(request):
	products = Product.objects.all()

	context = {'products':products}

	return render(request,'accounts/product.html',context)

def customer(request,pk_test):
	
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()

	context = {'customer':customer,'orders':orders}
	
	return render(request,'accounts/customer.html')