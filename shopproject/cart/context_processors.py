from.models import Cart, CartItem
from. views import _cart

def counter(request):
    icount=0
    if 'admin' in request.path:
        return {}
    else:
        try:

            cart=Cart.objects.filter(cart_id=_cart(request))
            cartitems=CartItem.objects.all().filter(cart=cart[:1])
            for ci in cartitems:
                icount+=ci.qty
        except Cart.DoesNotExist:
            icount=0
    return dict(icount=icount)
