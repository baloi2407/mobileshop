from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.views import View
from . models import Product, Brand, Customer, Cart, Payment, OrderPlaced, Wishlist
import razorpay
from django.contrib import messages
from django.db.models import Q, Count
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . forms import CustomerRegistrationForm, CustomerProfileForm
from . pagination import paginate_data
import uuid 
from . generate import generate_order_id, generate_numeric_order_id
from django.core.paginator import Paginator
# Create your views here.
#@login_required
def home(request):
    brands = Brand.objects.all()
    new_products = Product.objects.all().order_by('-updated_at')[:3]
    #print(new_products)
    popular_products = Product.objects.annotate(order_count=Count('orderplaced__prod_id')).order_by('-order_count')[:3]
    return render(request,'timezone-master/home.html',{'new_products': new_products,'popular_products': popular_products})

def about(request):
    return render(request,'timezone-master/about.html')

def contact(request):
    return render(request,'timezone-master/contact.html')

#@method_decorator(login_required,name='dispatch')
class BrandView(View):
    def get(self, request, val=None, page=1):
        # If there is no val parameter, query all products in descending order
        if val is not None:
            queryset = Product.objects.filter(brand_id=val).order_by('-updated_at')
        else:
            queryset = Product.objects.all().order_by('-updated_at')

        
        
        # Lấy các sản phẩm cho trang hiện tại
        products = paginate_data(queryset, request.GET.get('page'))

        return render(request, "timezone-master/category.html", locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(prod=product) & Q(user=request.user))
        return render(request,"timezone-master/product_details.html",locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm
        return render(request,"timezone-master/customer_registration.html",locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data!")
        return render(request,"timezone-master/customer_registration.html",locals())
    
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"timezone-master/profile.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data!")
        return render(request,"timezone-master/profile.html",locals())
    
def address(request):
    add = Customer.objects.filter(user_id=request.user)
    return render(request,"timezone-master/address.html",locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,"timezone-master/updateAddress.html",locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.first_name = form.cleaned_data['first_name']
            add.last_name = form.cleaned_data['last_name']
            add.email = form.cleaned_data['email']
            add.address = form.cleaned_data['address']
            add.date_of_birth = form.cleaned_data['date_of_birth']
            add.phone = form.cleaned_data['phone']
            if 'avatar' in request.FILES:
                avatar = request.FILES['avatar']
                add.avatar.save(avatar.name, avatar)
            add.save()
            messages.success(request,"Congratulations! Profile Update Successfully")
        else:
            messages.warning(request,"Invalid Input Data!")
        return redirect("address")

@login_required
def add_to_cart(request):
    if request.method == 'GET':
        user = request.user
        product_id = request.GET.get('prod_id')

        product = Product.objects.get(id=product_id)

        if product.quantity > 0:
            cart_item, created = Cart.objects.get_or_create(user=user, prod=product)

            if not created:
                cart_item.quantity += 1
                cart_item.save()

            # Thông báo thành công và chuyển hướng
            messages.success(request, 'Đã thêm sản phẩm vào giỏ hàng!')
            return redirect('/cart')
        else:
            # Thông báo hết hàng và giữ ở trang hiện tại
            messages.warning(request, 'Sản phẩm đã hết hàng.')
    
    # Giữ ở trang hiện tại
    return redirect(request.META.get('HTTP_REFERER', '/'))
        

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    
    
    # Lấy các sản phẩm cho trang hiện tại
    page_obj = paginate_data(cart, request.GET.get('page'))
    
    amount = 0
    for p in page_obj.object_list:
        value = p.quantity * p.prod.price
        amount += value
    
    return render(request, "timezone-master/add_to_cart.html", {'cart': page_obj, 'amount': amount})

def update_cart(request, action):
    if request.method == 'GET':
        if request.user.is_authenticated:
            prod_id = request.GET.get('prod_id')
            
            if prod_id:
                try:
                    c = Cart.objects.get(Q(prod=prod_id) & Q(user=request.user))
                    # Số lượng sản phẩm trong kho
                    available_quantity = c.prod.quantity
                    if action == "plus":
                        c.quantity += 1
                        
                    elif action == "minus":
                        if c.quantity > 1:
                            c.quantity -= 1
                    c.save()
                    
                    user = request.user
                    cart = Cart.objects.filter(user=user)
                    amount = 0
                    for p in cart:
                        value = p.quantity * p.prod.price
                        amount += value
                    
                    data = {
                        'quantity': c.quantity,
                        'amount': amount,
                    }
                    return JsonResponse(data)
                except Cart.DoesNotExist:
                    return JsonResponse({'error': 'Product not found in cart'}, status=400)
            else:
                return JsonResponse({'error': 'Invalid product ID'}, status=400)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
        
def remove_from_cart(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            prod_id = request.GET.get('prod_id')
            
            if prod_id:
                try:
                    c = Cart.objects.get(Q(prod=prod_id) & Q(user=request.user))
                    c.delete()  # Xóa sản phẩm khỏi giỏ hàng

                    user = request.user
                    cart = Cart.objects.filter(user=user)
                    amount = 0
                    for p in cart:
                        value = p.quantity * p.prod.price
                        amount += value
                    
                    data = {
                        'amount': amount,
                    }
                    return JsonResponse(data)
                except Cart.DoesNotExist:
                    return JsonResponse({'error': 'Product not found in cart'}, status=400)
            else:
                return JsonResponse({'error': 'Invalid product ID'}, status=400)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
        
class checkout(View):
    def get(self,request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        amount = 0
        for p in cart_items:
            value = p.quantity * p.prod.price * p.prod.discount if p.prod.discount > 0 else p.quantity * p.prod.price
            amount += value
        razoramount = int(amount)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data = {"amount":razoramount,"currency":"INR","receipt":"order_rcptid_12"}
        payment_response = client.order.create(data=data)
        print(payment_response)
        order_id = payment_response['id']
        print(order_id)
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user=user,
                amount=amount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
            payment.save()
        return render(request,"timezone-master/checkout.html",locals())

def payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    #print("payment_done : oid = ",order_id,"pid = ",payment_id,"cid = ",cust_id)
    user=request.user
    #return redirect("orders")
    customer=Customer.objects.get(id=cust_id)
    #To update payment status and payment id
    payment=Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    #To save order details
    cart = Cart.objects.filter(user=user)
    for c in cart:
        prod = Product.objects.get(prod=c.prod)
        prod.quantity -= c.quantity
        prod.save()
        OrderPlaced(user=user,customer=customer,prod=c.prod,quantity=c.quantity,payment=payment).save()
        c.delete()
    return redirect("orders")

def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request,"timezone-master/orders.html",locals())

def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user

        # Kiểm tra xem sản phẩm đã tồn tại trong wishlist của người dùng hay chưa
        if not Wishlist.objects.filter(user=user, prod__id=prod_id).exists():
            # Nếu sản phẩm chưa tồn tại trong wishlist, thì thêm mới
            product = Product.objects.get(id=prod_id)
            Wishlist(user=user, prod=product).save()
            data = {
                'message': 'Wishlist Added Successfully',
            }
        else:
            # Nếu sản phẩm đã tồn tại trong wishlist, trả về thông báo tương ứng
            data = {
                'message': 'Product already in your wishlist',
            }

        return JsonResponse(data)

def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = get_object_or_404(Product, id=prod_id)
        user = request.user
        message = ""

        if user.is_authenticated:
            try:
                wishlist = Wishlist.objects.get(user=user, prod=product)
                wishlist.delete()
                message = 'Removed from Wishlist'
            except Wishlist.DoesNotExist:
                message = 'Product was not in Wishlist'

        data = {
            'message': message,
        }

        return JsonResponse(data)

def show_wishlist(request):
    user = request.user
    product = Wishlist.objects.filter(user=user)
    return render(request,"timezone-master/wishlist.html",locals())

def search(request):
    query = request.GET['search']
    products = Product.objects.filter(Q(pro_name__icontains=query))
    return render(request,"timezone-master/search.html",locals())

def advanced_search(request):
    pro_name = request.GET.get('pro_name')
    brand = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Xây dựng truy vấn
    products = Product.objects.all()

    if pro_name:
        products = products.filter(pro_name__icontains=pro_name)

    if brand:
        # Tìm tên thương hiệu tương ứng với từ khóa người dùng
        matching_brands = Brand.objects.filter(brand_name__icontains=brand)
        
        # Lấy danh sách id của các thương hiệu tìm được
        brand_ids = matching_brands.values_list('id', flat=True)

        # Tìm các sản phẩm có brand_id trùng với id của các thương hiệu tìm được
        products = Product.objects.filter(brand__in=brand_ids)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, "timezone-master/search.html", {'products': products})
