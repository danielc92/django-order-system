from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm as RF
from django.http import HttpResponse
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout as authlogout
from django.contrib.auth import authenticate as auth
from django.contrib.auth.decorators import login_required as login_required
from .models import Product, Order, OrderProduct


@login_required
def home_view(request):

    context = {'objects': Product.objects.all() }

    return render(request, 'home.html', context)


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

    orders = OrderProduct.objects.all()

    context = {'data': orders}

    return render(request, 'summary.html', context)


@login_required
def add_to_cart(request, slug):

    product = get_object_or_404(Product, slug=slug)
    print(product)

    # Create the order
    order_queryset = Order.objects.filter(user=request.user, order_status=False)
    
    if order_queryset.exists():
        order = order_queryset[0]
        print("order stored, it exists already")
    else:
        order = Order.objects.create(user=request.user)
        print("order created, it didnt exist")
    
    # Add the items
    order_product = OrderProduct.objects.create(user=request.user, 
                                                product=product, 
                                                order=order)

    print('item added to order')

    return redirect('system:order-summary')



@login_required
def confirm_order(request):

    # Check for unconfirmed product level orders
    order_queryset = OrderProduct.objects.filter(user=request.user, confirmed=False)
    
    if order_queryset.exists():
        print("Items need to be flagged as confirmed")

        # First get the order ID
        order_id = order_queryset[0].order.id
        print(order_id)

        for order_product in order_queryset:
            order_product.confirmed = True
            order_product.save()
        
        order = Order.objects.filter(id=order_id)[0]

        print(order)
        order.order_status = True
        order.save()

        # Set all flags to confirmed in both OrderProduct and Order
    else:
        print("No outstanding items")


    return redirect('system:order-summary')
