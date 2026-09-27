from django.contrib.auth.decorators import login_required


@login_required
def shop(request):
    products_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'shop/shop.html', {'products': products})


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product')
    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total, })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('shop:cart')


@login_required
def increase_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.quantity += 1
    item.save()

    return redirect('shop:cart')


@login_required
def decrease_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('shop:cart')


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('shop:cart')


from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Product, CartItem, Order, OrderItem


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(
        user=request.user
    ).select_related('product')

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    if request.method == 'POST':

        if not cart_items.exists():
            return redirect('shop:cart')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company = request.POST.get('company')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        notes = request.POST.get('notes')

        with transaction.atomic():

            # ساخت سفارش
            order = Order.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                company=company,
                address=address,
                city=city,
                phone=phone,
                email=email,
                notes=notes,
                total=total,
            )

            # انتقال محصولات Cart به Order
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )

            # خالی کردن سبد خرید
            cart_items.delete()

        return redirect('shop:shop')

    return render(
        request,
        'shop/checkout.html',
        {
            'cart_items': cart_items,
            'total': total,
        }
    )
