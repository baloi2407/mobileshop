from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from .models import Product,Brand, Customer
from django.core.exceptions import ValidationError
import re

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

def validate_field(value, field_name):
    if not value:
        raise ValidationError(f"{field_name} cannot be left blank.")

    value = value.strip()

    if not value.isalnum():
        raise ValidationError(f"{field_name} cannot contain special characters.")

    if re.search(r'[^\x00-\x7F]+', value):
        raise ValidationError(f"{field_name} cannot contain Vietnamese accents.")

    if len(value) < 3:
        raise ValidationError(f"{field_name} is too short. {field_name} needs at least 3 characters.")

class BaseForm(forms.ModelForm):
    def clean_brand_name(self):
        brand_name = self.cleaned_data.get('brand_name')
        validate_field(brand_name, "Brand name")
        return brand_name

    def clean_pro_name(self):
        pro_name = self.cleaned_data.get('pro_name')
        validate_field(pro_name, "Pro name")
        return pro_name
    

class BrandForm(BaseForm):
    class Meta:
        model = Brand
        fields = '__all__'  # Use all fields from the model

    
    

class ProductForm(BaseForm):
    class Meta:
        model = Product
        fields = '__all__'  # Use all fields from the model

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("Price is required.")
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0.")
        return price

    def clean_discount(self):
        discount = self.cleaned_data.get('discount')
        if discount is None:
            raise forms.ValidationError("Discount is required.")
        if discount < 0 or discount >= 100:
            raise forms.ValidationError("Discount must be between 0 and 99.")
        return discount
    
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
    
    
   