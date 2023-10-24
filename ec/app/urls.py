from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static  # Import thêm static
from django.contrib.auth.views import LoginView, PasswordChangeView,PasswordChangeDoneView, LogoutView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . forms import LoginForm
from . forms import MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm

urlpatterns = [
    path('', views.home),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("category/<slug:val>",views.CatgoryView.as_view(),name="category"),
    path("category-title/<val>",views.CatgoryTitle.as_view(),name="category-title"),
    path("product-details/<int:pk>",views.ProductDetail.as_view(),name="product-details"),
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("address/",views.address,name="address"),
    path("updateAddress/<int:pk>",views.updateAddress.as_view(),name="updateAddress"),

    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='show-cart'),
    path('pluscart/', views.update_cart, {'action': 'plus'}),
    path('minuscart/', views.update_cart, {'action': 'minus'}),
    path('removecart/', views.remove_from_cart),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('orders/',views.orders,name='orders'),
    path('pluswishlist/', views.plus_wishlist),
    path('minuswishlist/', views.minus_wishlist),
    path('wishlist/', views.show_wishlist,name='showwishlist'),

    path('search/',views.search,name='search'),


    # Login authentication
    path("registration/",views.CustomerRegistrationView.as_view(),name="registration"),
    path("accounts/login/",LoginView.as_view(template_name='timezone-master/login.html',authentication_form = LoginForm),name="login"),
    
    path('password-change/', PasswordChangeView.as_view(template_name='timezone-master/passwordChange.html', form_class=MyPasswordChangeForm, success_url='/password-change-done'), name='password-change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name='timezone-master/passwordChangeDone.html'), name='password-change-done'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('password-reset/',PasswordResetView.as_view(template_name='timezone-master/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/',PasswordResetDoneView.as_view(template_name='timezone-master/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='timezone-master/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='timezone-master/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:  # Thêm điều kiện kiểm tra DEBUG mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Mobile Shop"
admin.site.site_title = "Mobile Shop"
admin.site.site_index_title = "Welcome to Mobile Shop"