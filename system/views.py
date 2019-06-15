from django.shortcuts import render
from .forms import RegisterForm as RF
from django.http import HttpResponse
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout as authlogout
from django.contrib.auth import authenticate as auth
from django.contrib.auth.decorators import login_required as lr



@lr
def home_view(request):

    context = {}

    return render(request, 'home.html', context)


def login_view(request):

    if request.method == 'POST':

        user = auth(request, 
        username=request.POST.get('uname'),
        password=request.POST.get('pass'))

        if user is not None:
            authlogin(request, user)
            return redirect('home')
        else:
            return HttpResponse('You have failed to login.')

    context = {}
    
    return render(request, 'login.html', context)



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

