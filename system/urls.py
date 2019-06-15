from django.urls import path
from .views import home_view, login_view, logout_view, register_view, order_summary, add_to_cart

app_name = 'system'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('', home_view, name='home'),
    path('order', order_summary, name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart')
]