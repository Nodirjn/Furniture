from django.urls import path

from app_products.views import ProductDetailView, ProductListView

app_name = 'products'
urlpatterns = [
    path('detail/', ProductDetailView.as_view(), name='detail'),
    path('', ProductListView.as_view(), name='list'),
]