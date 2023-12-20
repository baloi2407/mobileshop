from django.db import models  # Import để định nghĩa các mô hình dữ liệu cho ứng dụng

from django.contrib.auth.models import User  # Import để sử dụng chức năng quản lý người dùng và xác thực

from django.utils import timezone  # Import để làm việc với múi giờ và thời gian trong Django

from . uploads import (  # Import các hàm hoặc biến từ module uploads để xử lý tải lên hình ảnh hoặc tệp tin cho các thương hiệu, sản phẩm, danh mục, tin tức và hình đại diện
    upload_to_brand,
    upload_to_product,
    upload_to_avatar,
    upload_to_news_category,
    upload_to_news,
    upload_to_supplier,
    upload_to_about,
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
STATUS_PAID = (
    ('Not paid','Not paid'),
    ('Paid','Paid'),
)
STATUS_SELL = (
    ('Not sell','Not sell'),
    ('Sell','Sell'),
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

class CustomerAddress(models.Model):
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
        db_table = 'customer_addresses'
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
    customer = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)
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

class News_Category(models.Model):
    news_cat_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=upload_to_news_category, blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)   
    

    def __str__(self):
        return self.news_cat_name
    
    class Meta:
        db_table = 'news_categories'
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"

class News(models.Model):
    news_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_to_news, blank=True, null=True)
    news_cat = models.ForeignKey(News_Category, on_delete=models.CASCADE,blank=True, null=True)
    source = models.CharField(max_length=100,blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.news_name
    
    def get_news_cat_name(self):
        return self.news_cat.news_cat_name
    get_news_cat_name.short_description = 'News Category Name'
    
    class Meta:
        db_table = 'news'
        verbose_name = "News"
        verbose_name_plural = "News"

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    address = models.TextField(blank=True, null=True)
    owner = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to=upload_to_supplier, blank=True, null=True)
    summary = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)   
    

    def __str__(self):
        return self.supplier_name
    
    class Meta:
        db_table = 'suppliers'
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

class Warehouse_Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    amount = models.FloatField(blank=True,null=True)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,blank=True, null=True)
    paid = models.CharField(max_length=50,choices=STATUS_PAID, default='Not paid')
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)   
    
    def get_username(self):
        return self.user.username
    get_username.short_description = 'Username'

    def get_proname(self):
        return self.prod.pro_name
    get_proname.short_description = 'Product'

    def get_suppliername(self):
        return self.supplier.supplier_name
    get_suppliername.short_description = 'Supplier'
    
    class Meta:
        db_table = 'warehouse_payment'
        verbose_name = "Warehouse Payment"
        verbose_name_plural = "Warehouse Payment"

class Warehouse_Product(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,blank=True, null=True)
    note = models.TextField(blank=True,null=True)
    paid = models.CharField(max_length=50,choices=STATUS_SELL, default='Not sell')
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)   
    

    def get_proname(self):
        return self.prod.pro_name
    get_proname.short_description = 'Product'

    def get_suppliername(self):
        return self.supplier.supplier_name
    get_suppliername.short_description = 'Supplier'
    
    class Meta:
        db_table = 'warehouse_products'
        verbose_name = "Warehouse Product"
        verbose_name_plural = "Warehouse Product"

class About(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to=upload_to_about, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)   
    

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'about'
        verbose_name = "About"
        verbose_name_plural = "About"

class Contact(models.Model):
    company = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    fax = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)   
    

    def __str__(self):
        return self.company
    
    class Meta:
        db_table = 'contact'
        verbose_name = "Contact"
        verbose_name_plural = "Contact"