from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
STATUS = (
        ('Block', 'Block'),
        ('Active', 'Active'),
    )
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='brand', blank=True, null=True)
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
STATE_CHOICES = (
    ('hanoi', 'Hà Nội'),
    ('hochiminh', 'Hồ Chí Minh'),
    ('haiphong', 'Hải Phòng'),
    ('danang', 'Đà Nẵng'),
    ('hue', 'Huế'),
    ('nhatrang', 'Nha Trang'),
    ('cantho', 'Cần Thơ'),
    ('binhduong', 'Bình Dương'),
    ('quangninh', 'Quảng Ninh'),
    ('thanhhoa', 'Thanh Hóa'),
    ('nghean', 'Nghệ An'),
    ('hatinh', 'Hà Tĩnh'),
    ('quangbinh', 'Quảng Bình'),
    ('quangtri', 'Quảng Trị'),
    ('thuathienhue', 'Thừa Thiên Huế'),
    ('quangnam', 'Quảng Nam'),
    ('quangngai', 'Quảng Ngãi'),
    ('konturng', 'Kon Tum'),
    ('daklak', 'Đắk Lắk'),
    ('gia lai', 'Gia Lai'),
    ('daknong', 'Đắk Nông'),
    ('lamdong', 'Lâm Đồng'),
    ('binhphuoc', 'Bình Phước'),
    ('binhdinh', 'Bình Định'),
    ('phuyen', 'Phú Yên'),
    ('khanhhoa', 'Khánh Hòa'),
    ('ninhthuan', 'Ninh Thuận'),
    ('binhthuan', 'Bình Thuận'),
    ('dongnai', 'Đồng Nai'),
    ('tayninh', 'Tây Ninh'),
    ('longan', 'Long An'),
    ('anlong', 'An Giang'),
    ('dongsong', 'Đồng Tháp'),
    ('tiengiang', 'Tiền Giang'),
    ('bentre', 'Bến Tre'),
    ('travinh', 'Trà Vinh'),
    ('vungtau', 'Vũng Tàu'),
    ('kiengiang', 'Kiên Giang'),
    ('cambodia', 'Cà Mau'),
    ('hautinh', 'Hậu Giang'),
    ('sagiang', 'Sóc Trăng'),
    ('bacninh', 'Bắc Ninh'),
    ('bacgiang', 'Bắc Giang'),
    ('namdinh', 'Nam Định'),
    ('haiphong', 'Hải Phòng'),
    ('quangninh', 'Quảng Ninh'),
    ('ninhbinh', 'Ninh Bình'),
    ('thanhhoa', 'Thanh Hóa'),
    ('nghean', 'Nghệ An'),
    ('hatinh', 'Hà Tĩnh'),
    ('quangbinh', 'Quảng Bình'),
    ('quangtri', 'Quảng Trị'),
    ('thuathienhue', 'Thừa Thiên Huế'),
    ('quangnam', 'Quảng Nam'),
    ('quangngai', 'Quảng Ngãi'),
    ('konturng', 'Kon Tum'),
    ('daklak', 'Đắk Lắk'),
    ('gia lai', 'Gia Lai'),
    ('daknong', 'Đắk Nông'),
    ('lamdong', 'Lâm Đồng'),
    ('binhphuoc', 'Bình Phước'),
    ('binhdinh', 'Bình Định'),
    ('phuyen', 'Phú Yên'),
    ('khanhhoa', 'Khánh Hòa'),
    ('ninhthuan', 'Ninh Thuận'),
    ('binhthuan', 'Bình Thuận'),
    ('dongnai', 'Đồng Nai'),
    ('tayninh', 'Tây Ninh'),
    ('longan', 'Long An'),
    ('anlong', 'An Giang'),
    ('dongsong', 'Đồng Tháp'),
    ('tiengiang', 'Tiền Giang'),
    ('bentre', 'Bến Tre'),
    ('travinh', 'Trà Vinh'),
    ('vungtau', 'Vũng Tàu'),
    ('kiengiang', 'Kiên Giang'),
    ('cambodia', 'Cà Mau'),
    ('hautinh', 'Hậu Giang'),
    ('sagiang', 'Sóc Trăng'),
    # Add other cities that are relevant to you here
)


class Product(models.Model):
    pro_name = models.CharField(max_length=100,blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    summary = models.CharField(max_length=100,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='brand', blank=True, null=True)
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
    email = models.CharField(max_length=100,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'customers'
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

class Cart(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)

    @property
    def total_cost(self):
        return self.quantity * self.prod.price
    
    class Meta:
        db_table = 'cart'
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payment'
        verbose_name = "Payment"
        verbose_name_plural = "Payment"
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
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
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlist'
        verbose_name = "Wish List"
        verbose_name_plural = "Wish List"

