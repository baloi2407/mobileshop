from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from . models import Product,Customer, Cart, Payment, OrderPlaced, Wishlist
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def home(request):
    return render(request,'timezone-master/home.html')

def about(request):
    return render(request,'timezone-master/about.html')

def contact(request):
    return render(request,'timezone-master/contact.html')

@method_decorator(login_required,name='dispatch')
class CatgoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"timezone-master/category.html",locals())
    
class CatgoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"timezone-master/category.html",locals())
  
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
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
    add = Customer.objects.filter(user=request.user)
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
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations! Profile Update Successfully")
        else:
            messages.warning(request,"Invalid Input Data!")
        return redirect("address")
    


class checkout(View):
    def get(self,request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        amount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            amount += value
        razoramount = int(amount)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data = {"amount":razoramount,"currency":"INR","receipt":"order_rcptid_12"}
        payment_response = client.order.create(data=data)
        #print(payment_response)
        order_id = payment_response['id']
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
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
        c.delete()
    return redirect("orders")

def add_to_cart(request):
    if request.method == 'GET':
        user = request.user
        product_id = request.GET.get('prod_id')
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect('/cart')

        cart_item, created = Cart.objects.get_or_create(user=user, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    return render(request,"timezone-master/add_to_cart.html",locals())

def update_cart(request, action):
    if request.method == 'GET':
        if request.user.is_authenticated:
            prod_id = request.GET.get('prod_id')
            
            if prod_id:
                try:
                    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
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
                        value = p.quantity * p.product.discounted_price
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
                    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
                    c.delete()  # Xóa sản phẩm khỏi giỏ hàng

                    user = request.user
                    cart = Cart.objects.filter(user=user)
                    amount = 0
                    for p in cart:
                        value = p.quantity * p.product.discounted_price
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
        
def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request,"timezone-master/orders.html",locals())

def plus_wishlist(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user,product=product).save()
        data={
            'message':'Wishlist Added Successfully',
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
                wishlist = Wishlist.objects.get(user=user, product=product)
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
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request,"timezone-master/search.html",locals())