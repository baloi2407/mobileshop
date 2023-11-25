from django.db import models  # Import để định nghĩa các mô hình dữ liệu cho ứng dụng

from django.contrib.auth.models import User  # Import để sử dụng chức năng quản lý người dùng và xác thực

from django.utils import timezone  # Import để làm việc với múi giờ và thời gian trong Django

from . uploads import (  # Import các hàm hoặc biến từ module uploads để xử lý tải lên hình ảnh hoặc tệp tin cho các thương hiệu, sản phẩm, danh mục, tin tức và hình đại diện
    upload_to_brand,
    upload_to_product,
    upload_to_avatar,
)

from django.core.exceptions import ValidationError  # Import ngoại lệ để xử lý các tình huống đặc biệt trong quá trình xây dựng ứng dụng


# Create your models here.
STATUS = (
        ('Block', 'Block'),
        ('Active', 'Active'),
    )

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=upload_to_brand, blank=True, null=True)
    sku = models.CharField(max_length=100,blank=True,null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)   
    

    def __str__(self):
        return self.brand_name
    
    class Meta:
        db_table = 'brands'
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Product(models.Model):
    pro_name = models.CharField(max_length=100,blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    summary = models.CharField(max_length=100,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_to_product, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,blank=True, null=True)
    display_size = models.CharField(max_length=50,blank=True, null=True)
    os = models.CharField(max_length=50,blank=True, null=True)
    rear_camera = models.CharField(max_length=50,blank=True, null=True)
    front_camera = models.CharField(max_length=20,blank=True, null=True)
    chip = models.CharField(max_length=50,blank=True, null=True)
    ram = models.CharField(max_length=50,blank=True, null=True)
    storage = models.CharField(max_length=50,blank=True, null=True)
    sim = models.CharField(max_length=100,blank=True, null=True)
    battery_capacity = models.CharField(max_length=50,blank=True, null=True)
    sku = models.CharField(max_length=100,blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pro_name
    
    def get_brand_name(self):
        return self.brand.brand_name
    get_brand_name.short_description = 'Brand Name'
    
    class Meta:
        db_table = 'products'
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Customer(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'customers'
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

class Cart(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    value = models.FloatField(blank=True,null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def total_cost(self):
        return self.quantity * self.prod.price
    
    class Meta:
        db_table = 'cart'
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200,blank=True, null=True)
    amount = models.FloatField()
    address = models.TextField(blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=20, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Payment ID: {self.id} - Created At: {self.created_at}"
    
    class Meta:
        db_table = 'payment'
        verbose_name = "Payment"
        verbose_name_plural = "Payment"

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    value = models.FloatField(blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    @property 
    def total_cost(self):
        return self.quantity * self.prod.price
    
    class Meta:
        db_table = 'orderplaced'
        verbose_name = "Order Placed"
        verbose_name_plural = "Order Placed"

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'wishlist'
        verbose_name = "Wish List"
        verbose_name_plural = "Wish List"
# Bỏ qua
# class Category(models.Model):
#     cat_name = models.CharField(max_length=100)
#     summary = models.CharField(max_length=100,blank=True,null=True)
#     image = models.ImageField(upload_to=upload_to_category, blank=True, null=True)
#     content = models.TextField(blank=True,null=True)
#     sku = models.CharField(max_length=100,blank=True,null=True)
#     alias = models.CharField(max_length=100, blank=True, null=True)
#     title = models.CharField(max_length=100,blank=True,null=True)
#     description = models.TextField(blank=True,null=True)
#     status = models.CharField(max_length=50, choices=STATUS, default='Active')
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)    

#     def __str__(self):
#         return self.cat_name
    
#     class Meta:
#         db_table = 'categories'
#         verbose_name = "Category"
#         verbose_name_plural = "Categories"

# class News(models.Model):
#     news_name = models.CharField(max_length=100,blank=True, null=True)
#     summary = models.CharField(max_length=100,blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to=upload_to_news, blank=True, null=True)
#     cat = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
#     sku = models.CharField(max_length=100,blank=True, null=True)
#     alias = models.CharField(max_length=100, blank=True, null=True)
#     title = models.CharField(max_length=100,blank=True,null=True)
#     description = models.TextField(blank=True,null=True)
#     status = models.CharField(max_length=50, choices=STATUS, default='Active')
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.news_name
    
#     def get_cat_name(self):
#         return self.cat.cat_name
#     get_cat_name.short_description = 'Cat Name'
    
#     class Meta:
#         db_table = 'news'
#         verbose_name = "News"
#         verbose_name_plural = "News"

class Avatar(models.Model):
    
    image = models.ImageField(upload_to=upload_to_avatar, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'avatars'
        verbose_name = "Avatar"
        verbose_name_plural = "Avatars"

    def save(self, *args, **kwargs):
        # Kiểm tra xem người dùng đã có avatar hay chưa
        existing_avatar = Avatar.objects.filter(user=self.user).exists()
        if existing_avatar and not self.pk:
            raise ValidationError('This user already has an avatar.')  # Nếu người dùng đã có avatar, không cho phép tạo mới

        super(Avatar, self).save(*args, **kwargs)

