from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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


CATEGORY_CHOICES=(
    ('AP','Apple'),
    ('SS','Samsung'),
    ('OP','Oppo'),
    ('HW','Huawei'),
    ('XM','Xiaomi'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    @property 
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)