from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def buy_now(request, pk):
    # Buy Now ക്ലിക്ക് ചെയ്യുമ്പോൾ ആ പ്രൊഡക്റ്റ് മാത്രം താൽക്കാലികമായി കാർട്ടിൽ സെറ്റ് ചെയ്ത് നേരെ ചെക്കൗട്ടിലേക്ക് വിടുന്നു
    cart = {str(pk): 1}
    request.session['cart'] = cart
    return redirect('checkout')

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout(request):
    cart = request.session.get('cart', {})
    total_price = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        total_price += product.price * quantity

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method', 'COD')
        upi_id = request.POST.get('upi_id', '')

        Order.objects.create(
            name=name,
            phone=phone,
            address=address,
            total_price=total_price,
            payment_method=payment_method,
            upi_id=upi_id
        )

        request.session['cart'] = {}
        return render(request, 'order_success.html', {'payment_method': payment_method})
    
    return render(request, 'checkout.html', {'total_price': total_price})