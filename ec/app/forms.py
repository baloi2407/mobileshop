from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from .models import Product,Brand, Customer, Category, News, Cart, OrderPlaced, Payment, Wishlist
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from datetime import date
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))



class BaseForm(forms.ModelForm):
    @staticmethod
    def validate_field(value, field_name):
        if not value:
            raise ValidationError(f"{field_name} cannot be left blank.")

        value = value.strip()
    
        value_without_whitespace = value.replace(" ", "")  # Xóa khoảng trắng
        if not value_without_whitespace.isalnum():
            raise ValidationError(f"{field_name} cannot contain special characters.")
        
        if re.search(r'[^\x00-\x7F]+', value):
            raise ValidationError(f"{field_name} cannot contain Vietnamese accents.")

        if len(value) < 3:
            raise ValidationError(f"{field_name} is too short. {field_name} needs at least 3 characters.")
        
    def clean_field(self, field_name):
        field_value = self.cleaned_data.get(field_name)
        BaseForm.validate_field(field_value, field_name)
        return field_value
    @staticmethod
    def validate_positive_value(value, field_name):
        if value is None:
            raise forms.ValidationError(f"{field_name} is required.")
        if value <= 0:
            raise forms.ValidationError(f"{field_name} must be greater than 0.")
        return value
    @staticmethod
    def validate_discount(value, field_name):
        if value is None:
            raise forms.ValidationError(f"{field_name} is required.")
        if value < 0 or value >= 100:
            raise forms.ValidationError(f"{field_name} must be between 0 and 99.")
        return value
    @staticmethod
    def validate_email(value, field_name):
        try:
            validate_email(value)
        except ValidationError as e:
            raise forms.ValidationError(f"{field_name} is not a valid email address.")

        return value
    @staticmethod
    def validate_phone(value, field_name):
        if value is None:
            return value  # Cho phép giá trị rỗng

        value_str = str(value)
        if not value_str.isdigit():
            raise forms.ValidationError(f"{field_name} must only contain digits.")

        if not (10 <= len(value_str) <= 11):
            raise forms.ValidationError(f"{field_name} must have 10 or 11 digits.")

        return value
    @staticmethod
    def validate_date_of_birth(value, field_name):
        if value:
            # Kiểm tra xem năm có lớn hơn hoặc bằng năm hiện tại không
            if value.year >= date.today().year:
                raise forms.ValidationError(f"{field_name.capitalize()} phải nhỏ hơn năm hiện tại.")

            # Kiểm tra định dạng
            try:
                value.strftime('%Y-%m-%d')
            except ValueError:
                raise forms.ValidationError(f"Định dạng {field_name} không hợp lệ. Sử dụng 'YYYY-MM-DD'.")

        return value
    def clean_selected_field(self, field_name):
        field_value = self.cleaned_data.get(field_name)
        if not field_value:
            raise forms.ValidationError(f"{field_name} is required.")
        return field_value
    
class BrandForm(BaseForm):
    class Meta:
        model = Brand
        fields = '__all__'  # Use all fields from the model
    def clean_brand_name(self):
        return self.clean_field('brand_name')
    

class ProductForm(BaseForm):
    class Meta:
        model = Product
        fields = '__all__'  # Use all fields from the model
    def clean_pro_name(self):
        return self.clean_field('pro_name')

    # Sử dụng hàm validate_positive_value cho các trường price và quality
    def clean_price(self):
        return self.validate_positive_value(self.cleaned_data.get('price'), "Price")

    

    # Sử dụng hàm validate_discount cho trường discount
    def clean_discount(self):
        return self.validate_discount(self.cleaned_data.get('discount'), "Discount")
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('brand')
        return cleaned_data

class CategoryForm(BaseForm):
    class Meta:
        model = Category
        fields = '__all__'  # Use all fields from the model
    def clean_cat_name(self):
        return self.clean_field('cat_name')
    
class NewsForm(BaseForm):
    class Meta:
        model = News
        fields = '__all__'  # Use all fields from the model
    def clean_news_name(self):
        return self.clean_field('news_name')
    
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('cat')
        return cleaned_data
    
class CustomerForm(BaseForm):
    class Meta:
        model = Customer
        fields = '__all__'  # Use all fields from the model
    def clean_first_name(self):
        return self.clean_field('first_name')
    
    def clean_last_name(self):
        return self.clean_field('last_name')
    
    def clean_email(self):
        return self.validate_email(self.cleaned_data.get('email'), "Email")
    
    def clean_phone(self):
        return self.validate_phone(self.cleaned_data.get('phone'), "Phone")
    
    def clean_date_of_birth(self):
        return self.validate_date_of_birth(self.cleaned_data.get('date_of_birth'), "Date of birth")
    
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('user')
        return cleaned_data

class CartForm(BaseForm):
    class Meta:
        model = Cart
        fields = '__all__'  # Use all fields from the model
    def clean_quantity(self):
        return self.validate_positive_value(self.cleaned_data.get('quantity'), "Quantity") 
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('user')
        self.clean_selected_field('prod')
        return cleaned_data

    
class OrderPlacedForm(BaseForm):
    class Meta:
        model = OrderPlaced
        fields = '__all__'  # Use all fields from the model
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('user')
        self.clean_selected_field('customer')
        self.clean_selected_field('prod')
        return cleaned_data

class PaymentForm(BaseForm):
    class Meta:
        model = Payment
        fields = '__all__'  # Use all fields from the model
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('user')
        return cleaned_data
    def clean_amount(self):
        return self.validate_positive_value(self.cleaned_data.get('amount'), "Amount") 

class WishlistForm(BaseForm):
    class Meta:
        model = Wishlist
        fields = '__all__'  # Use all fields from the model
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('user')
        self.clean_selected_field('prod')
        return cleaned_data
    

    
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','email','address','date_of_birth','phone','avatar']
        widgets={
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputfirst_name', 'placeholder': 'first_name', 'type': 'text'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputlast_name', 'placeholder': 'last_name', 'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputemail', 'placeholder': 'email', 'type': 'email'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputaddress', 'placeholder': 'address', 'type': 'address'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputphone', 'placeholder': 'Phone','type':'phone'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),

        }
    
    
   