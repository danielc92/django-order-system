from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm as RF
from django.http import HttpResponse
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout as authlogout
from django.contrib.auth import authenticate as auth
from django.contrib.auth.decorators import login_required as login_required
from .models import Product, Order, OrderProduct
from django.db.models import Avg, Sum, Count

@login_required
def home_view(request):

    context = {'objects': Product.objects.all() }

    return render(request, 'home.html', context)


@login_required
def logout_view(request):
    authlogout(request)

    return redirect('system:login')


def login_view(request):

    if request.method == 'POST':

        user = auth(request, 
        username=request.POST.get('username'),
        password=request.POST.get('password'))

        if user is not None:
            authlogin(request, user)
            return redirect('system:home')
        else:
            return HttpResponse('You have failed to login.')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('system:home')

    return render(request, 'login.html')



def register_view(request):

    if request.method == 'POST':
        form = RF(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
            
    else:
        form = RF()

    context = {'form': form}
    
    return render(request, 'register.html', context)

@login_required
def order_summary(request):

    orders = OrderProduct.objects.filter(user=request.user)

    unconfirmed_orders = OrderProduct.objects.filter(user=request.user, confirmed=False)

    total = unconfirmed_orders.aggregate(Sum('product__price'))

    items = unconfirmed_orders.aggregate(Sum('quantity'))

    context = {'data': orders, 'total': total, 'items': items}

    return render(request, 'summary.html', context)


@login_required
def add_to_cart(request, slug):

    # Store the product object, given a slug
    product = get_object_or_404(Product, slug=slug)

    # Create or store Order object based on conditional
    order_queryset = Order.objects.filter(user=request.user, order_status=False)
    
    if order_queryset.exists():
        order = order_queryset[0]
    else:
        order = Order.objects.create(user=request.user)
    
    # Create OrderProduct given the above objects
    order_product = OrderProduct.objects.create(user=request.user, 
                                                product=product, 
                                                order=order)

    return redirect('system:order-summary')



@login_required
def confirm_order(request):

    # Check for unconfirmed product level orders
    order_queryset = OrderProduct.objects.filter(user=request.user, confirmed=False)
    
    if order_queryset.exists():

        # First get the order ID
        order_id = order_queryset[0].order.id
        print(order_id)

        # Update ProductOrders Objects
        for order_product in order_queryset:
            order_product.confirmed = True
            order_product.save()
        
        # Update the Order Object
        order = Order.objects.filter(id=order_id)[0]
        order.order_status = True
        order.save()

    else:
        print("No outstanding items")

    return redirect('system:order-summary')
