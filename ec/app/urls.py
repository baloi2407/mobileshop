from django.urls import path  # Import để sử dụng chức năng routing (định tuyến URL) trong Django

from django.contrib import admin  # Import để sử dụng trang quản trị của Django

from . import views  # Import các views (chế độ xem) từ module hiện tại của ứng dụng

from django.conf import settings  # Import cài đặt settings của Django để sử dụng các cấu hình

from django.conf.urls.static import static  # Import để cấu hình tĩnh (static) trong URL

from django.contrib.auth.views import (  # Import các views liên quan đến xác thực và quản lý mật khẩu của người dùng trong Django
    LoginView,
    PasswordChangeView,
    PasswordChangeDoneView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from . forms import (  # Import các biểu mẫu từ module forms trong cùng thư mục để sử dụng trong ứng dụng
    LoginForm,
    MyPasswordChangeForm,
    MyPasswordResetForm,
    MySetPasswordForm,
)

# Tạo các urls


urlpatterns = [
    path('', views.home),
    path("home/", views.home,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("brand/<int:val>/",views.BrandView.as_view(),name="brand"),
    path("brand/",views.BrandView.as_view(),name="brand-default"),
    path("product-details/<int:pk>",views.ProductDetail.as_view(),name="product-details"),

    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("address/",views.address,name="address"),
    path("createAddress/",views.createAddressView.as_view(),name="createAddress"),
    path("updateAddress/<int:pk>",views.updateAddress.as_view(),name="updateAddress"),
    path("deleteAddress/<int:pk>",views.deleteAddress,name="deleteAddress"),
    path("avatar/",views.avatar,name="avatar"),
    path("uploadAvatar/",views.avatar,name="uploadAvatar"),
    path("updateAvatar/<int:pk>",views.updateAvatar.as_view(),name="updateAvatar"),
    path("deleteAvatar/<int:pk>",views.deleteAvatar,name="deleteAvatar"),

    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='show-cart'),
    path('pluscart/', views.update_cart, {'action': 'plus'}),
    path('minuscart/', views.update_cart, {'action': 'minus'}),
    path('removecart/', views.remove_from_cart),

    
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('orders/',views.orders,name='orders'),
    path('order_details/<int:payment_id>/',views.order_details,name='order_details'),

    path('pluswishlist/', views.plus_wishlist),
    path('minuswishlist/', views.minus_wishlist),
    path('wishlist/', views.show_wishlist,name='showwishlist'),

    path('search/',views.search,name='search'),
    path('advanced_search/', views.advanced_search, name='advanced_search'),

    path("news/<int:val>/",views.News_CategoryView.as_view(),name="news"),
    path("news/",views.News_CategoryView.as_view(),name="news-default"),
    path("news-details/<int:pk>",views.NewsDetail.as_view(),name="news-details"),
    path('search-news/',views.search_news,name='search-news'),

    path('user-email/',views.UserEmail,name='user-email'),
    path('update-email/',views.update_email,name='update-email'),

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