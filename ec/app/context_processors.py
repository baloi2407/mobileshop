from . models import Brand,Product, Cart, Wishlist,Avatar


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

def avatar(request):
    avatar_url = None

    if request.user.is_authenticated:
        latest_avatar = Avatar.objects.filter(user=request.user,is_used=1).order_by('-updated_at').first()
        if latest_avatar:
            avatar_url = latest_avatar.image.url

    return {'avatar': avatar_url}