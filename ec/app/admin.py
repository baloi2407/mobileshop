from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import Group
from . models import Product, Brand, Customer, Cart, Payment, OrderPlaced, Wishlist,Category,News, Avatar
from .forms import ProductForm,BrandForm,CustomerForm,CategoryForm,NewsForm, CartForm, WishlistForm, OrderPlacedForm, PaymentForm,AvatarAdminForm
from .mixins import Mixins

from .resources import ProductResource
from import_export.admin import ImportExportModelAdmin
# # Register your models here.

class BaseAdmin(ImportExportModelAdmin,admin.ModelAdmin, Mixins):
    list_per_page = settings.LIST_PER_PAGE
    actions = [Mixins.make_active,Mixins.make_block,Mixins.export_to_excel]
@admin.register(Brand)
class BrandModelAdmin(BaseAdmin):
    list_display = ['id', 'brand_name', 'summary', 'display_image', 'sku', 'status', 'updated_at'] 
    search_fields = ['id', 'brand_name', 'sku']
    form = BrandForm

@admin.register(Product)
class ProductModelAdmin(BaseAdmin):
    list_display = ['id','pro_name','get_brand_name','formatted_price','formatted_discount','display_image','status','updated_at']
    search_fields = ['id', 'pro_name', 'sku','brand__brand_name']
    form = ProductForm
    

@admin.register(Customer)
class CustomerModelAdmin(BaseAdmin):
    list_display = ['id','first_name','email','phone','status','updated_at']
    search_fields = ['id','first_name','email','phone']
    form = CustomerForm

@admin.register(Cart)
class CartModelAdmin(BaseAdmin):
    list_display = ['id','user','products','quantity','updated_at']
    search_fields = ['id','user__id']
    form = CartForm
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.prod.pk])
        return format_html('<a href="{}">{}</a>',link, obj.prod.pro_name)
    
@admin.register(Payment)
class PaymentModelAdmin(BaseAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid','updated_at']
    search_fields = ['id','user__id','user__username']
    form = PaymentForm

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(BaseAdmin):
    list_display = ['id','user','customers','products','quantity','status','payments','updated_at']
    search_fields = ['id','user__id','user__username','prod__pro_name']
    form = OrderPlacedForm
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.prod.pk])
        return format_html('<a href="{}">{}</a>',link, obj.prod.pro_name)
    def customers(self,obj):
        link = reverse("admin:app_customer_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link, obj.customer.email)
    def payments(self,obj):
        link = reverse("admin:app_payment_change",args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>',link, obj.payment.id)
    payments.short_description = 'Payment ID'

@admin.register(Wishlist)
class WishlistModelAdmin(BaseAdmin):
    list_display = ['id','user','products','updated_at']
    search_fields = ['id','user__username','prod__pro_name']
    form = WishlistForm
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.prod.pk])
        return format_html('<a href="{}">{}</a>',link, obj.prod.pro_name)

@admin.register(Category)
class CategoryModelAdmin(BaseAdmin):
    list_display = ['id', 'cat_name', 'summary', 'display_image', 'sku', 'status', 'updated_at']
    search_fields = ['id', 'cat_name', 'sku']
    form = CategoryForm

@admin.register(News)
class NewsModelAdmin(BaseAdmin):
    list_display = ['id','news_name','get_cat_name','display_image','status','updated_at']
    search_fields = ['id','news_name','cat__cat_name']
    form = NewsForm

@admin.register(Avatar)
class AvatarModelAdmin(BaseAdmin):
    list_display = ['id','display_image','user_id','is_used_display','status','updated_at']
    form = AvatarAdminForm

    
#admin.site.unregister(Group)

