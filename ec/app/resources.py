from import_export import resources
from .models import Product, Brand, Customer, Cart, Payment, OrderPlaced, Wishlist

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
class CartResource(resources.ModelResource):
    class Meta:
        model = Cart
class PaymentResource(resources.ModelResource):
    class Meta:
        model = Payment
class OrderPlacedResource(resources.ModelResource):
    class Meta:
        model = OrderPlaced
class WishlistResource(resources.ModelResource):
    class Meta:
        model = Wishlist
