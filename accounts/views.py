from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .filters import OrderFilter

# Create your views here.

def registerPage(request):

	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')

	context = {'form':form}

	return render(request,'accounts/register.html',context)

def loginPage(request):
	context = {

	}

	return render(request,'accounts/login.html',context)

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

	orders_count = orders.count()

	myFilter = OrderFilter(request.GET,queryset=orders)
	orders = myFilter.qs

	context = {'customer':customer,'orders':orders,'orders_count':orders_count,
				'myFilter':myFilter}
	
	return render(request,'accounts/customer.html',context)

def createOrder(request,pk):
	customer = Customer.objects.get(id=pk)
	form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'accounts/order_form.html',context)

def updateOrder(request,pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request,'accounts/order_form.html',context)

def deleteOrder(request,pk):
	order = Order.objects.get(id=pk)
	if request.method =='POST':
		order.delete()
		return redirect('/')


	context = {'item':order}

	return render(request, 'accounts/delete.html', context)