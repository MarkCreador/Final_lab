from django.urls import path
from .views import *

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    
    # Brand URLs
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('brands/create/', BrandCreateView.as_view(), name='brand-create'),
    path('brands/<int:pk>/update/', BrandUpdateView.as_view(), name='brand-update'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand-delete'),

    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),

    # Order URLs
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),

    # OrderItem URLs
    path('orderitems/', OrderItemListView.as_view(), name='orderitem-list'),
    path('orderitems/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),
    path('orderitems/create/', OrderItemCreateView.as_view(), name='orderitem-create'),
    path('orderitems/<int:pk>/update/', OrderItemUpdateView.as_view(), name='orderitem-update'),
    path('orderitems/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='orderitem-delete'),
    
    

    

    
]