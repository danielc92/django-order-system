from django.shortcuts import render

# Create your views here.

def home_view(request):

    context = {}

    return render(request, 'home.html', context)


def login_view(request):

    context = {}
    
    return render(request, 'login.html', context)



def register_view(request):

    context = {}
    
    return render(request, 'register.html', context)

