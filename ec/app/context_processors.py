from . models import Brand,Product, Cart, Wishlist


def brands(request):
    brands = Brand.objects.all()

    return {'brands': brands}

def cart_items(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return {'totalitem': totalitem}

def wish_items(request):
    wishitems = 0
    if request.user.is_authenticated:
        wishitems = len(Wishlist.objects.filter(user=request.user))
    return {'wishitems': wishitems}