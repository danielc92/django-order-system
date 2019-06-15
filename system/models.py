from django.db import models
from django.conf import settings
from django.shortcuts import redirect, reverse



class Product(models.Model):

    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    discounted = models.FloatField()
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField()

    product_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def add_to_cart(self):
        return reverse('system:add-to-cart', kwargs={'slug':self.slug})

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_status = models.BooleanField(default=False)
    order_started = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"


class OrderProduct(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} units of {self.product.product_name}"



