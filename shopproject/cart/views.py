from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from shopapp.models import product
from .models import Cart,CartItem

# Create your views here.
def _cart(request):
    cart=request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def add_cart(request,pro_id):
    Product=product.objects.get(id=pro_id)
    try:
        cart=Cart.objects.get(cart_id= _cart(request))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart(request))
        cart.save()
    try:
        cartitem =CartItem.objects.get(products=Product,cart=cart)
        cartitem.qty +=1
        cartitem.save()
    except CartItem.DoesNotExist:
        cartitem=CartItem.objects.create(products=Product,qty=1 , cart=cart)
        cartitem.save()
    return redirect('cart:cartdetail')

def cartdetail(request,total=0,counter=0,cartitems=None):
    try:

        cart=Cart.objects.get(cart_id=_cart(request))
        cartitems=CartItem.objects.filter(cart=cart,active=True)
        for ci in cartitems:
            total+=(ci.products.price * ci.qty)
            counter += ci.qty
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cartitems=cartitems,total=total,counter=counter))

def remove(request,pro_id):
    cart=Cart.objects.get(cart_id=_cart(request))
    Product=get_object_or_404(product,id=pro_id)
    cartitem=CartItem.objects.get(products=Product,cart=cart)
    if cartitem.qty >1:
        cartitem.qty-=1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cart:cartdetail')

def delete(request,pro_id):
    cart=Cart.objects.get(cart_id=_cart(request))
    Product=get_object_or_404(product,id=pro_id)
    cartitem=CartItem.objects.get(products=Product,cart=cart)
    cartitem.delete()
    return redirect('cart:cartdetail')



