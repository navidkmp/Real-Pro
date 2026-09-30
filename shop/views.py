from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, CartItem, Order, OrderItem, Coupon


@login_required
def shop(request):
    products_list = Product.objects.all().order_by('-created_at')

    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(
        request,
        'shop/shop.html',
        {
            'products': products,
        }
    )


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(
        user=request.user
    ).select_related('product')


    subtotal = sum(
        item.product.price * item.quantity
        for item in cart_items
    )


    coupon_code = request.session.get('coupon_code')
    discount_percent = request.session.get(
        'discount_percent',
        0
    )

    discount = (
        subtotal
        * Decimal(str(discount_percent))
        / Decimal('100')
    )

    total = subtotal - discount

    return render(
        request,
        'shop/cart.html',
        {
            'cart_items': cart_items,
            'subtotal': subtotal,
            'discount': discount,
            'discount_percent': discount_percent,
            'coupon_code': coupon_code,
            'total': total,
        }
    )


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    return redirect('shop:shop')


@login_required
def increase_cart(request, item_id):
    item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect('shop:cart')


@login_required
def decrease_cart(request, item_id):
    item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
        return redirect('shop:shop')

    return redirect('shop:cart')


@login_required

def remove_from_cart(request, item_id):
    item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    item.delete()
    if not CartItem.objects.filter(user=request.user).exists():
        return redirect('shop:shop')


    return redirect('shop:cart')


@login_required
def check_coupon(request):

    if request.method != 'POST':
        return redirect('shop:cart')

    code = request.POST.get(
        'coupon',
        ''
    ).strip().upper()

    if not code:
        request.session.pop('coupon_code', None)
        request.session.pop('discount_percent', None)

        return redirect('shop:cart')

    try:
        coupon = Coupon.objects.get(
            code=code,
            active=True
        )

    except Coupon.DoesNotExist:

        request.session.pop('coupon_code', None)
        request.session.pop('discount_percent', None)


        return redirect('shop:cart')

    if coupon.used_by.filter(
        id=request.user.id
    ).exists():

        request.session.pop('coupon_code', None)
        request.session.pop('discount_percent', None)

        return redirect('shop:cart')

    request.session['coupon_code'] = coupon.code
    request.session['discount_percent'] = str(
        coupon.discount_percent
    )

    return redirect('shop:cart')


@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    ).select_related('product')


    if not cart_items.exists():
        return redirect('shop:cart')

    subtotal = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    coupon_code = request.session.get('coupon_code')
    discount_percent = request.session.get(
        'discount_percent',
        0
    )

    coupon = None

    if coupon_code:

        try:
            coupon = Coupon.objects.get(
                code=coupon_code,
                active=True
            )

        except Coupon.DoesNotExist:

            request.session.pop('coupon_code', None)
            request.session.pop('discount_percent', None)

            coupon_code = None
            discount_percent = 0

        else:

            if coupon.used_by.filter(
                id=request.user.id
            ).exists():

                request.session.pop('coupon_code', None)
                request.session.pop('discount_percent', None)

                coupon = None
                coupon_code = None
                discount_percent = 0


    discount = (
        subtotal
        * Decimal(str(discount_percent))
        / Decimal('100')
    )

    total = subtotal - discount

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company = request.POST.get('company')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        notes = request.POST.get('notes')

        with transaction.atomic():

            if coupon:

                coupon = Coupon.objects.select_for_update().get(
                    id=coupon.id
                )

                if coupon.used_by.filter(
                    id=request.user.id
                ).exists():
                    return redirect('shop:cart')

                discount = (
                    subtotal
                    * coupon.discount_percent
                    / Decimal('100')
                )

                total = subtotal - discount

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

            for item in cart_items:

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )

            if coupon:
                coupon.used_by.add(request.user)

            cart_items.delete()

        request.session.pop('coupon_code', None)
        request.session.pop('discount_percent', None)

        return redirect('home:home')

    return render(
        request,
        'shop/checkout.html',
        {
            'cart_items': cart_items,
            'subtotal': subtotal,
            'discount': discount,
            'discount_percent': discount_percent,
            'coupon_code': coupon_code,
            'total': total,
        }
    )