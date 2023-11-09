from django.contrib import admin
from . models import Product, Brand, Customer, Cart, Payment, OrderPlaced, Wishlist
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group
from .forms import ProductForm,BrandForm
from .mixins import Mixins
from django.conf import settings
# # Register your models here.

class BaseAdmin(admin.ModelAdmin, Mixins):
    list_per_page = settings.LIST_PER_PAGE
    actions = [Mixins.make_active,Mixins.make_block]
@admin.register(Brand)
class BrandModelAdmin(BaseAdmin):
    list_display = ['id', 'brand_name', 'summary', 'display_image', 'sku', 'status', 'updated_at']
    form = BrandForm

@admin.register(Product)
class ProductModelAdmin(BaseAdmin):
    list_display = ['id','pro_name','get_brand_name','formatted_price','formatted_discount','display_image','status','updated_at']
    form = ProductForm
    list_per_page = settings.LIST_PER_PAGE

@admin.register(Customer)
class CustomerModelAdmin(BaseAdmin):
    list_display = ['id','first_name','email','phone','status','updated_at']
    list_per_page = settings.LIST_PER_PAGE

@admin.register(Cart)
class CartModelAdmin(BaseAdmin):
    list_display = ['id','user','products','quantity']
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.prod.pk])
        return format_html('<a href="{}">{}</a>',link, obj.prod.pro_name)
    
@admin.register(Payment)
class PaymentModelAdmin(BaseAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(BaseAdmin):
    list_display = ['id','user','customers','products','quantity','status','payments']
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.prod.pk])
        return format_html('<a href="{}">{}</a>',link, obj.prod.pro_name)
    def customers(self,obj):
        link = reverse("admin:app_customer_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link, obj.customer.email)
    def payments(self,obj):
        link = reverse("admin:app_payment_change",args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>',link, obj.payment.id)

@admin.register(Wishlist)
class WishlistModelAdmin(BaseAdmin):
    list_display = ['id','user','products']
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.prod.pk])
        return format_html('<a href="{}">{}</a>',link, obj.prod.pro_name)

#admin.site.unregister(Group)

