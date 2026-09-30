from home.models import Footer
from shop.models import CartItem


def cart_context(request):
    cart_count = 0

    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()

    return {
        'cart_count': cart_count,
    }


def footer_links(request):
    footer = Footer.objects.first()
    return {'footer': footer}