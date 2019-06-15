from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponse

# Create your views here.


def home_view(request):

    context = {}

    return render(request, 'home.html', context)


def login_view(request):

    context = {}
    
    return render(request, 'login.html', context)



def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
            
    else:
        form = RegisterForm()

    context = {'form': form}
    
    return render(request, 'register.html', context)

