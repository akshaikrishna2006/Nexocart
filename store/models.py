from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default='general')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  # Main image
    stock = models.IntegerField(default=10)            # Extra detail: Stock
    specifications = models.TextField(blank=True, null=True)  # Extra detail: Specs
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Product-inu extra pictures add cheyyan ulla model
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/extra/')

    def __str__(self):
        return f"{self.product.name} Image"

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, default='COD')
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.name}"