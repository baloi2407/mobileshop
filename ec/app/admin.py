from django.contrib import admin  # Import để sử dụng trang quản trị của Django

from django.utils.html import format_html  # Import để định dạng HTML trong Django

from django.urls import reverse  # Import để tạo các đường dẫn (URL) động trong Django

from django.conf import settings  # Import cài đặt settings của Django để sử dụng các cấu hình

from . models import (  # Import các mô hình từ module models trong cùng thư mục để sử dụng trong ứng dụng
    Product,
    Brand,
    CustomerAddress,
    Cart,
    Payment,
    OrderPlaced,
    Wishlist,
    Avatar,
    News_Category,
    News,
    Supplier,
    Warehouse_Payment,
    Warehouse_Product,
    Contact,
    About,
)

from .forms import (  # Import các biểu mẫu từ module forms trong cùng thư mục để sử dụng trong ứng dụng
    ProductForm,
    BrandForm,
    CustomerForm,
    CartForm,
    WishlistForm,
    OrderPlacedForm,
    PaymentForm,
    AvatarAdminForm,
)

from .mixins import Mixins  # Import Mixins từ module mixins trong cùng thư mục để sử dụng trong ứng dụng

from django.db.models import Sum, Q  # Import để sử dụng các chức năng liên quan đến truy vấn và tính toán trên mô hình dữ liệu

from django.utils.translation import gettext_lazy as _  # Import để sử dụng gettext_lazy để đảm bảo hỗ trợ ngôn ngữ đa nền trong Django

from import_export.admin import ImportExportModelAdmin  # Import để sử dụng ImportExportModelAdmin trong quản trị Django cho việc nhập và xuất dữ liệu


# Đăng ký models


class BaseAdmin(ImportExportModelAdmin,admin.ModelAdmin, Mixins):
    list_per_page = settings.LIST_PER_PAGE
    actions = [Mixins.make_active,Mixins.make_block,Mixins.export_to_excel]
@admin.register(Brand)
class BrandModelAdmin(BaseAdmin):
    list_display = ['id', 'brand_name', 'summary', 'display_image', 'sku', 'status', 'updated_at'] 
    search_fields = ['id', 'brand_name', 'sku']
    list_filter = ('status',
        ('created_at', admin.DateFieldListFilter), 
    )
    form = BrandForm

@admin.register(Product)
class ProductModelAdmin(BaseAdmin):
    list_display = ['id','pro_name','get_brand_name','quantity','formatted_price','formatted_discount','display_image','status','updated_at']
    search_fields = ['id', 'pro_name', 'sku','brand__brand_name']
    list_filter = ('status','brand__brand_name',
        ('created_at', admin.DateFieldListFilter), 
    )
    form = ProductForm
    

@admin.register(CustomerAddress)
class CustomerModelAdmin(BaseAdmin):
    list_display = ['id','first_name','last_name','phone','status','updated_at']
    search_fields = ['id','first_name','last_name','phone']
    list_filter = ('status',
        ('created_at', admin.DateFieldListFilter), 
    )
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
    list_display = ['id','user','amount','customer_name','address','phone','paid','status','updated_at']
    search_fields = ['id','user__id','user__username']
    list_filter = ('status','paid',
        ('created_at', admin.DateFieldListFilter), 
    )
    date_hierarchy = 'created_at'    
    form = PaymentForm    

    def get_filters_params(self, request):
        filters_params = {}
        for param, value in request.GET.items():
            if param.startswith('status__'):
                filters_params['status__exact'] = value
            elif param.startswith('paid__'):
                filters_params['paid__exact'] = value
            elif param.startswith('created_at__'):
                filters_params[param] = value
        return filters_params
    change_list_template = 'admin/payment/change_list.html'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)
        queryset = self.get_queryset(request)

        # Trích xuất các tham số lọc từ request.GET
        filters_params = self.get_filters_params(request)

        # Lọc queryset dựa trên các tham số lọc
        if 'status__exact' in filters_params and 'paid__exact' in filters_params and 'created_at__gte' in filters_params and 'created_at__lt' in filters_params:
            queryset = queryset.filter(
                Q(status=filters_params['status__exact']) &
                Q(paid=filters_params['paid__exact']) &
                Q(created_at__gte=filters_params['created_at__gte']) &
                Q(created_at__lt=filters_params['created_at__lt'])
            )
        elif 'status__exact' in filters_params and 'paid__exact' in filters_params:
            queryset = queryset.filter(status=filters_params['status__exact'], paid=filters_params['paid__exact'])
        elif 'created_at__gte' in filters_params and 'created_at__lt' in filters_params:
            queryset = queryset.filter(created_at__gte=filters_params['created_at__gte'], created_at__lt=filters_params['created_at__lt'])
        elif 'status__exact' in filters_params:
            queryset = queryset.filter(status=filters_params['status__exact'])
        elif 'paid__exact' in filters_params:
            queryset = queryset.filter(paid=filters_params['paid__exact'])

        # Tính tổng số tiền của các đối tượng Payment trong queryset đã được lọc
        total_amount = queryset.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

        total_quality = queryset.count()
        extra_context = {
            'total_amount': total_amount,
            'total_quality': total_quality,
        }

        return super().changelist_view(request, extra_context=extra_context)


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(BaseAdmin):
    list_display = ['id','user','customers','products','quantity','status','payments','updated_at']
    search_fields = ['id','user__id','user__username','prod__pro_name']
    list_filter = ('status','prod__pro_name',
        ('created_at', admin.DateFieldListFilter), 
    )
    date_hierarchy = 'created_at'
    form = OrderPlacedForm
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.prod.pk])
        return format_html('<a href="{}">{}</a>',link, obj.prod.pro_name)
    def customers(self,obj):
        link = reverse("admin:app_customeraddress_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link, obj.customer.first_name)
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


@admin.register(Avatar)
class AvatarModelAdmin(BaseAdmin):
    list_display = ['id','display_image','user_id','status','updated_at']
    form = AvatarAdminForm

@admin.register(News_Category)
class NewsCategoryModelAdmin(BaseAdmin):
    list_display = ['id', 'news_cat_name', 'summary', 'content', 'display_image', 'status', 'updated_at'] 
    search_fields = ['id', 'news_cat_name','created_at']
    list_filter = ('status',
        ('created_at', admin.DateFieldListFilter), 
    )

@admin.register(News)
class NewsModelAdmin(BaseAdmin):
    list_display = ['id', 'news_name','get_news_cat_name', 'summary', 'content', 'display_image', 'status', 'updated_at'] 
    search_fields = ['id', 'news_name','news_cat__news_cat_name','created_at']
    list_filter = ('status','news_cat__news_cat_name',
        ('created_at', admin.DateFieldListFilter), 
    )

@admin.register(Supplier)
class SupplierModelAdmin(BaseAdmin):
    list_display = ['id', 'supplier_name','email', 'phone', 'status', 'updated_at'] 
    search_fields = ['id', 'supplier_name','created_at']
    list_filter = ('status','supplier_name',
        ('created_at', admin.DateFieldListFilter), 
    )

@admin.register(Warehouse_Payment)
class Warehouse_PaymentModelAdmin(BaseAdmin):
    list_display = ['id', 'get_username','amount', 'get_proname','quantity','get_suppliername', 'status', 'updated_at'] 
    search_fields = ['id', 'supplier__supplier_name','prod__pro_name','created_at']
    list_filter = ('status','supplier__supplier_name','prod__pro_name',
        ('created_at', admin.DateFieldListFilter), 
    )

@admin.register(Warehouse_Product)
class Warehouse_ProductModelAdmin(BaseAdmin):
    list_display = ['id','products','get_suppliername', 'status', 'updated_at'] 
    search_fields = ['id', 'supplier__supplier_name','prod__pro_name','created_at']
    list_filter = ('status','supplier__supplier_name','prod__pro_name',
        ('created_at', admin.DateFieldListFilter), 
    )
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.prod.pk])
        return format_html('<a href="{}">{}</a>',link, obj.prod.pro_name)

@admin.register(Contact)
class ContactModelAdmin(BaseAdmin):
    list_display = ['id', 'company','phone', 'email','address','fax', 'status', 'updated_at'] 
    search_fields = ['id', 'company','phone', 'email','address','fax','created_at']
   

@admin.register(About)
class AboutModelAdmin(BaseAdmin):
    list_display = ['id', 'title','summary', 'content','display_image', 'status', 'updated_at'] 
    search_fields = ['id', 'title','created_at']


#admin.site.unregister(Group)
