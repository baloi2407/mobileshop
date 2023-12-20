from django.shortcuts import render, redirect, get_object_or_404  # Import các hàm render, redirect, get_object_or_404 từ Django để xử lý phản hồi và truy cập dữ liệu

from django.http import JsonResponse  # Import để tạo phản hồi dạng JSON

from django.views import View  # Import để sử dụng lớp View của Django để tạo các view (chế độ xem)

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
    Contact,
    About
)


import razorpay  # Import để sử dụng gói razorpay cho thanh toán

from django.contrib import messages  # Import để hiển thị thông báo hoặc tin nhắn trong Django

from django.db.models import Q, Count  # Import để thực hiện các truy vấn phức tạp với Q objects và tính toán số lượng với Count

from django.conf import settings  # Import cài đặt settings của Django để sử dụng các cấu hình

from django.contrib.auth.decorators import login_required # Import để bảo vệ view cần đăng nhập để truy cập


from django.utils.decorators import method_decorator

from urllib.parse import urlencode  # Import để mã hóa các thông tin URL

from . forms import (  # Import các biểu mẫu từ module forms trong cùng thư mục để sử dụng trong ứng dụng
    CustomerRegistrationForm,
    CustomerProfileForm,
    AvatarProfileForm,
)

from . pagination import paginate_data  # Import hàm paginate_data từ module pagination để phân trang dữ liệu
from django.contrib.auth.forms import UserChangeForm
# Tạo các views

#hàm xử lý view trang home
def home(request):
    brands = Brand.objects.all() # lấy tất cả các brand
    new_products = Product.objects.all().order_by('-updated_at')[:3]
    #print(new_products)
    popular_products = Product.objects.annotate(order_count=Count('orderplaced__prod_id')).order_by('-order_count')[:3]
    most_popular_product = Product.objects.annotate(order_count=Count('orderplaced__prod_id')).order_by('-order_count').first()

    return render(request,'timezone-master/home.html',locals())

#hàm xử lý view trang about
def about(request):
    about = About.objects.filter(status="Active").order_by('-updated_at').first()
    return render(request,'timezone-master/about.html',locals())

#hàm xử lý view trang contact
def contact(request):
    contact = Contact.objects.filter(status="Active").order_by('-updated_at').first()
    return render(request,'timezone-master/contact.html',locals())

#hàm xử lý view trang brand(Hiển thị danh sách sản phẩm theo nhãn)
class BrandView(View):
    def get(self, request, val=None, page=1):
        # If there is no val parameter, query all products in descending order
        if val is not None:
            queryset = Product.objects.filter(brand_id=val).order_by('-updated_at')
        else:
            queryset = Product.objects.all().order_by('-updated_at')        
        
        # Lấy các sản phẩm cho trang hiện tại
        products = paginate_data(queryset, request.GET.get('page'))

        return render(request, "timezone-master/brand.html", locals())

#Xử lý view trang chi tiết sản phẩm
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        brand_name = product.brand.brand_name
        wishlist = Wishlist.objects.filter(Q(prod=product) & Q(user=request.user))
        return render(request,"timezone-master/product_details.html",locals())
    
#Xử lý view trang đăng ký tài khoản
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm
        return render(request,"timezone-master/customer_registration.html",locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
            return redirect("/accounts/login/")
        else:
            messages.warning(request,"Invalid Input Data!")
            return render(request,"timezone-master/customer_registration.html",locals())
        


@method_decorator(login_required,name='dispatch')
#Xử lý view trang prodfile user(phát triển sau)
class ProfileView(View):
    pass

        
@login_required    
#Xử lý view trang địa chỉ
def address(request):
    try:
        add = CustomerAddress.objects.get(user=request.user)
    except CustomerAddress.DoesNotExist:
        add = None

    return render(request,"timezone-master/address.html",locals())

#Thêm thông tin địa chỉ cho tài khoản
@method_decorator(login_required,name='dispatch')
class createAddressView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"timezone-master/createAddress.html",locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST, request.FILES)  # Phải bao gồm `request.FILES` cho các trường dạng file
        if form.is_valid():
            user = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            address = form.cleaned_data['address']
            date_of_birth = form.cleaned_data['date_of_birth']
            phone = form.cleaned_data['phone']

            # Tạo một bản ghi mới của CustomerAddress
            CustomerAddress.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                address=address,
                date_of_birth=date_of_birth,
                phone=phone
            )
     
            messages.success(request, "Congratulations! Profile Saved Successfully")

            return redirect('/address')

        else:
            messages.warning(request, "Invalid Input Data!")
            return render(request, "timezone-master/profile.html", {'form': form})

#Xử lý view trang cập nhật thông tin địa chỉ
class updateAddress(View):
    def get(self,request,pk):
        add = CustomerAddress.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,"timezone-master/updateAddress.html",locals())
    
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = CustomerAddress.objects.get(pk=pk)
            add.first_name = form.cleaned_data['first_name']
            add.last_name = form.cleaned_data['last_name']
            add.address = form.cleaned_data['address']
            add.date_of_birth = form.cleaned_data['date_of_birth']
            add.phone = form.cleaned_data['phone']
            
            add.save()
            messages.success(request,"Congratulations! Profile Update Successfully")
        else:
            messages.warning(request,"Invalid Input Data!")

        return redirect(request.META.get('HTTP_REFERER', '/'))
    
@login_required
#Xử lý view xóa thông tin địa chỉ
def deleteAddress(request,pk):
    customer = get_object_or_404(CustomerAddress, pk=pk)  # Lấy đối tượng Customer từ database hoặc trả về 404 nếu không tìm thấy

    try:
        # Xóa đối tượng Customer
        CustomerAddress.delete()  # Xóa khách hàng từ cơ sở dữ liệu
        messages.success(request, "Customer Deleted Successfully")
    except Exception as e:
        messages.error(request, f"Error deleting customer: {str(e)}")
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
#Xử lý view trang ảnh đại diện
def avatar(request):
    try:
        ava = Avatar.objects.get(user=request.user)
    except Avatar.DoesNotExist:
        # Create a new Avatar object for the user if it doesn't exist
        ava = Avatar.objects.create(user=request.user)
    return render(request,"timezone-master/avatar.html",locals())

@method_decorator(login_required,name='dispatch')
#Xử lý view trang cập nhật ảnh đại diện
class updateAvatar(View):
    def get(self,request,pk):
        ava = Avatar.objects.get(pk=pk)
        form = AvatarProfileForm(instance=ava)
        return render(request,"timezone-master/updateAvatar.html",locals())
    
    def post(self,request,pk):
        form = AvatarProfileForm(request.POST)
        if form.is_valid():
            ava = Avatar.objects.get(pk=pk)
            
            if 'image' in request.FILES:
                image = request.FILES['image']
                ava.image.save(image.name, image)
            ava.save()
            messages.success(request,"Congratulations! Profile Update Successfully")
        else:
            messages.warning(request,"Invalid Input Data!")

        return redirect(request.META.get('HTTP_REFERER', '/'))
    
@login_required
#Xử lý view xóa ảnh đại diện
def deleteAvatar(request, pk):
    avatar = get_object_or_404(Avatar, pk=pk)  # Lấy đối tượng Avatar từ database hoặc trả về 404 nếu không tìm thấy

    try:
        # Xóa đối tượng Avatar
        avatar.image.delete()  # Xóa hình ảnh từ cơ sở dữ liệu
        messages.success(request, "Avatar Deleted Successfully")
    except Exception as e:
        messages.error(request, f"Error deleting avatar: {str(e)}")
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
#Xử lý view thêm sản phẩm vào giỏ
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
        
@login_required
#Xử lý view trang giỏ hàng
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user).order_by('id')
    
    
    # Lấy các sản phẩm cho trang hiện tại
    page_obj = paginate_data(cart, request.GET.get('page'))
    
    amount = 0
    for p in page_obj.object_list:
        p.value = p.quantity*(p.prod.price * (1 - p.prod.discount/100))
        amount += p.value 
        p.save()
    
    return render(request, "timezone-master/add_to_cart.html", {'cart': page_obj, 'amount': amount})

@login_required
#Xử lý view khi cập nhật giỏ hàng
def update_cart(request, action):
    if request.method == 'GET':
        if request.user.is_authenticated:
            prod_id = request.GET.get('prod_id')
            
            if prod_id:
                try:
                    c = Cart.objects.get(Q(prod=prod_id) & Q(user=request.user))
                    product = c.prod  # Lấy đối tượng Product từ Cart
                    
                    # Số lượng sản phẩm trong kho
                    available_quantity = c.prod.quantity
                    
                    # Kiểm tra action và kiểm tra xem có đủ số lượng trong kho hay không
                    if action == "plus" and available_quantity > c.quantity:
                        c.quantity += 1
                        c.save()
                        
                        user = request.user
                        cart = Cart.objects.filter(user=user)
                        amount = 0
                        for p in cart:
                            p.value = p.quantity*(p.prod.price * (1 - p.prod.discount/100))
                            p.save()
                            amount += p.value
                        
                      
                        
                        data = {
                            'quantity': c.quantity,
                            'amount': amount,
                        }
                        return JsonResponse(data)
                    elif action == "minus":
                        if c.quantity > 1:
                            c.quantity -= 1
                            c.save()
                        
                            user = request.user
                            cart = Cart.objects.filter(user=user)
                            amount = 0
                            for p in cart:
                                p.value = p.quantity*(p.prod.price * (1 - p.prod.discount/100))
                                p.save()
                                amount += p.value
                 
                            
                            data = {
                                'quantity': c.quantity,
                                'amount': amount,
                            }
                            return JsonResponse(data)
                        else:
                            return JsonResponse({'error': 'Invalid action or quantity'}, status=400)
                            
                    else:
                        return JsonResponse({'error': f'Not enough quantity in stock for {product.pro_name}'}, status=400)

                
                except Cart.DoesNotExist:
                    return JsonResponse({'error': 'Product not found in cart'}, status=400)
            else:
                return JsonResponse({'error': 'Invalid product ID'}, status=400)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
        
@login_required   
#Xử lý view xóa sản phẩm khỏi giỏ
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
                        amount += p.value
                    
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
        
@method_decorator(login_required,name='dispatch')  
#Xử lý view khi thanh toán   
class checkout(View):
    def get(self,request):
        user = request.user
        
        try:
            add = CustomerAddress.objects.get(user=user)
        except CustomerAddress.DoesNotExist:
            return redirect('/address')
        cart_items = Cart.objects.filter(user=user)
        if cart_items:
            amount = 0
            for p in cart_items:
                amount += p.value
            razoramount = int(amount)
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
            data = {"amount":razoramount,"currency":"INR","receipt":"order_rcptid_12"}
            payment_response = client.order.create(data=data)
            #print(payment_response)
            order_id = payment_response['id']
            #print(order_id)
            if order_id:
                order_status = payment_response['status']
                if order_status == 'created':
                    payment = Payment(
                        user=user,
                        amount=amount,
                        customer_name = f"{add.first_name} {add.last_name}" if add.first_name and add.last_name else add.first_name or add.last_name or "Unknown",
                        address = add.address,
                        phone = add.phone,
                        razorpay_order_id=order_id,
                        razorpay_payment_status=order_status
                    )
                    payment.save()
                return render(request,"timezone-master/checkout.html",locals())
            else:
                return redirect('/cart')
        else:
            return redirect('/cart')
            
    

#Xử lý view thanh toán hoàn thành
def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    user = request.user
    
    customer = CustomerAddress.objects.get(id=cust_id)
    payment = Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    
    cart = Cart.objects.filter(user=user)
    for c in cart:
        # Sử dụng trực tiếp đối tượng sản phẩm từ giỏ hàng
        prod = c.prod
        prod.quantity -= c.quantity
        prod.save()
        
        OrderPlaced(user=user, customer=customer, prod=prod, quantity=c.quantity,value=c.value, payment=payment).save()
        c.delete()
        
    return redirect("orders")


#Xử lý view trang đơn hàng
def orders(request):
    queryset = Payment.objects.filter(user=request.user).order_by('-id')
    # Lấy các sản phẩm cho trang hiện tại
    order_placed = paginate_data(queryset, request.GET.get('page'))
    
    return render(request,"timezone-master/orders.html",locals())


#Xử lý view trang chi tiết đơn hàng, 1 đơn hàng có thế có nhiều hơn 1 sản phẩm
def order_details(request, payment_id):
    queryset = OrderPlaced.objects.filter(user=request.user,payment=payment_id).order_by('id')
    # Lấy các sản phẩm cho trang hiện tại
    order_placed = paginate_data(queryset, request.GET.get('page'))
    
    return render(request,"timezone-master/order_details.html",locals())

@login_required
#Xử lý view thêm sản phẩm yêu thích
def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        user_id = request.user.id if request.user.is_authenticated else None

        if prod_id and user.is_authenticated:  # Kiểm tra xem người dùng có đăng nhập hay không
            product = Product.objects.filter(id=prod_id).first()  # Lấy đối tượng Product dựa trên prod_id

            if product:
                # Kiểm tra xem sản phẩm đã tồn tại trong wishlist của người dùng hay chưa
                if not Wishlist.objects.filter(user=user, prod=product).exists():
                    # Nếu sản phẩm chưa tồn tại trong wishlist, thêm mới
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
            else:
                # Xử lý khi không tìm thấy sản phẩm với prod_id cụ thể
                return JsonResponse({'message': 'Product not found'}, status=404)
        else:
            return JsonResponse({'message': 'User not authenticated'}, status=401)

@login_required
#Xử lý view xóa sản phẩm yêu thích
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

@login_required
#Xử lý view trang xem danh sách sản phẩm yêu thích
def show_wishlist(request):
    queryset = Wishlist.objects.filter(user=request.user).order_by('id')
    products = paginate_data(queryset, request.GET.get('page'))
    return render(request,"timezone-master/wishlist.html",locals())

#Xử lý view trang tìm kiếm
def search(request):
    query = request.GET['search']
    page_number = request.GET.get('page') or 1
    if query:
        search_params = urlencode({'search': query, 'page': page_number})
        search_url = f"/search/?{search_params}"  # Tạo URL chứa thông tin tìm kiếm và số trang

        queryset = Product.objects.filter(Q(pro_name__icontains=query)).order_by('id')
        # Lấy các sản phẩm cho trang hiện tại
        products = paginate_data(queryset, request.GET.get('page'))
        return render(request,"timezone-master/search.html",locals())
    else:
        return redirect('/brand')

#Xử lý view trang tìm kiếm nâng cao
def advanced_search(request):
    pro_name = request.GET.get('pro_name')
    brand = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    page_number = request.GET.get('page') or 1
    # Xây dựng truy vấn
    products = Product.objects.all().order_by('id')

    if pro_name:
        products = products.filter(pro_name__icontains=pro_name)

    if brand:
        # Tìm tên thương hiệu tương ứng với từ khóa người dùng
        matching_brands = Brand.objects.filter(brand_name__icontains=brand)
        
        # Lấy danh sách id của các thương hiệu tìm được
        brand_ids = matching_brands.values_list('id', flat=True)

        # Tìm các sản phẩm có brand_id trùng với id của các thương hiệu tìm được
        products = Product.objects.filter(brand__in=brand_ids).order_by('id')

    if min_price:
        products = products.filter(price__gte=min_price).order_by('id')

    if max_price:
        products = products.filter(price__lte=max_price).order_by('id')
    
    search_params = urlencode({'pro_name': pro_name,'brand': brand,'min_price': min_price,'max_price': max_price, 'page': page_number})
    search_url = f"/advanced_search/?{search_params}"  # Tạo URL chứa thông tin tìm kiếm và số trang
    # Lấy các sản phẩm cho trang hiện tại
    products = paginate_data(products, request.GET.get('page'))

    return render(request,"timezone-master/advanced_search.html",locals())


class News_CategoryView(View):
    def get(self, request, val=None, page=1):
        # If there is no val parameter, query all products in descending order
        if val is not None:
            queryset = News.objects.filter(news_cat_id=val).order_by('-updated_at')
        else:
            queryset = News.objects.all().order_by('-updated_at')        
        
        # Lấy các sản phẩm cho trang hiện tại
        news = paginate_data(queryset, request.GET.get('page'))

        return render(request, "timezone-master/news.html", locals())

#Xử lý view trang chi tiết sản phẩm
class NewsDetail(View):
    def get(self,request,pk):
        news = News.objects.get(pk=pk)
        news_cat_name = news.news_cat.news_cat_name
        return render(request,"timezone-master/news_details.html",locals())

#Xử lý view trang tìm kiếm tin tức
def search_news(request):
    query = request.GET['search']
    page_number = request.GET.get('page') or 1
    if query:
        search_params = urlencode({'search': query, 'page': page_number})
        search_url = f"/search/?{search_params}"  # Tạo URL chứa thông tin tìm kiếm và số trang

        queryset = News.objects.filter(Q(news_name__icontains=query)).order_by('id')
        # Lấy các sản phẩm cho trang hiện tại
        news = paginate_data(queryset, request.GET.get('page'))
        return render(request,"timezone-master/search_news.html",locals())
    else:
        return redirect('/news')

def UserEmail(request):
    return render(request,"timezone-master/user_email.html",locals())

@login_required
def update_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('email')
        request.user.email = new_email
        request.user.save()
        messages.success(request, 'Email updated successfully!')
        return redirect('/user-email')  
    return render(request,"timezone-master/user_email.html",locals())