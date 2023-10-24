from . models import Cart,Wishlist
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