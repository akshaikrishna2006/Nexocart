from django.contrib import admin
from .models import Category, Product, ProductImage, Order

admin.site.register(Category)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Multiple extra pictures upload cheyyan 3 extra slots nalkunnu

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    inlines = [ProductImageInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'total_price', 'payment_method', 'created_at')
    search_fields = ('name', 'phone')