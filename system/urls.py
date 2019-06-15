from django.urls import path
from .views import home_view, login_view, register_view

app_name = 'system'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('', home_view, name='home')
]