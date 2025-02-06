from django.urls import path

from app_pages.views import HomeTemplateView, ProductsTemplateView, ProductDetailTemplateView, UserWishlistTemplateView, \
    ContactCreateView

app_name = 'pages'

urlpatterns = [
    path('products/', ProductsTemplateView.as_view(), name='product'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    # path('product-detail/', ProductDetailTemplateView.as_view(), name='product'),
    # path('user-wishlist/', UserWishlistTemplateView.as_view(), name='product'),
    path('', HomeTemplateView.as_view(), name='home'),
]
