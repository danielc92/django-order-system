from django.db import models

# Create your models here.
class Product(models.Model):

    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    discounted = models.FloatField()
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField()

    product_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class OrderProduct(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_status = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} units of {self.product.product_name}"

class Order(models.Model):
    products = models.ManyToManyField(Product)

    order_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"