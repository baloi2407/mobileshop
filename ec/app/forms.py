from django import forms  # Import để sử dụng các forms trong Django

from django.contrib.auth.forms import (  # Import các forms liên quan đến xác thực người dùng trong Django
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
    SetPasswordForm,
    PasswordResetForm,
)

from django.contrib.auth.models import User  # Import mô hình User từ Django để quản lý người dùng

from .models import (  # Import các mô hình từ module models trong cùng thư mục để sử dụng trong ứng dụng
    Product,
    Brand,
    CustomerAddress,
    Cart,
    OrderPlaced,
    Payment,
    Wishlist,
    Avatar,
)

from django.core.exceptions import ValidationError  # Import ngoại lệ để xử lý các tình huống đặc biệt trong quá trình xây dựng ứng dụng

from django.core.validators import validate_email  # Import để xác thực địa chỉ email

import re  # Import để sử dụng thư viện re (regular expression)

from datetime import date  # Import để làm việc với dữ liệu thời gian và ngày tháng trong Python


#Tạo các forms 

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

        if len(value) < 2:
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
        fields = '__all__'  # Sử dụng tất cả các trường có trong model
    def clean_brand_name(self):
        return self.clean_field('brand_name')
    

class ProductForm(BaseForm):
    class Meta:
        model = Product
        fields = '__all__'  # Sử dụng tất cả các trường có trong model
    def clean_pro_name(self):
        return self.clean_field('pro_name')

    # Sử dụng hàm validate_positive_value cho các trường price và quality
    def clean_price(self):
        return self.validate_positive_value(self.cleaned_data.get('price'), "Price")

    def clean_quantity(self):
        return self.validate_positive_value(self.cleaned_data.get('quantity'), "Quantity")

    # Sử dụng hàm validate_discount cho trường discount
    def clean_discount(self):
        return self.validate_discount(self.cleaned_data.get('discount'), "Discount")
    
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('brand')
        return cleaned_data

    
class CustomerForm(BaseForm):
    class Meta:
        model = CustomerAddress
        fields = '__all__'  # Sử dụng tất cả các trường có trong model
    def clean_first_name(self):
        return self.clean_field('first_name')
    
    def clean_last_name(self):
        return self.clean_field('last_name')
    
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
        fields = '__all__'  # Sử dụng tất cả các trường có trong model
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
        fields = '__all__'  # Sử dụng tất cả các trường có trong model
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('user')
        self.clean_selected_field('customer')
        self.clean_selected_field('prod')
        return cleaned_data

class PaymentForm(BaseForm):
    class Meta:
        model = Payment
        fields = '__all__'  # Sử dụng tất cả các trường có trong model
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('user')
        return cleaned_data
    def clean_amount(self):
        return self.validate_positive_value(self.cleaned_data.get('amount'), "Amount") 

class WishlistForm(BaseForm):
    class Meta:
        model = Wishlist
        fields = '__all__'  # Sử dụng tất cả các trường có trong model
    def clean(self):
        cleaned_data = super().clean()
        self.clean_selected_field('user')
        self.clean_selected_field('prod')
        return cleaned_data
    
class AvatarAdminForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'
    
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

class CustomerProfileForm(BaseForm):
    def clean_first_name(self):
        return self.clean_field('first_name')

    def clean_last_name(self):
        return self.clean_field('last_name')
    
    def clean_date_of_birth(self):
        value = self.cleaned_data.get('date_of_birth')
        field_name = 'date_of_birth'
        return self.validate_date_of_birth(value, field_name)
    
    class Meta:
        model = CustomerAddress
        fields = ['first_name','last_name','address','date_of_birth','phone']
        widgets={
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputfirst_name', 'placeholder': 'first_name', 'type': 'text'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputlast_name', 'placeholder': 'last_name', 'type': 'text'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputaddress', 'placeholder': 'address', 'type': 'address'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputphone', 'placeholder': 'Phone','type':'text'}),

        }

    

class AvatarProfileForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

 