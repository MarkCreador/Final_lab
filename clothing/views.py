from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Brand, Product, Customer, Order, OrderItem
from .forms import  CategoryForm, BrandForm, ProductForm, CustomerForm, OrderForm, OrderItemForm
# Create your views here.

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            categories = paginator.page(page)
        except PageNotAnInteger:
            categories = paginator.page(1)
        except EmptyPage:
            categories = paginator.page(paginator.num_pages)

        return categories

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')  # URL to redirect after successful form submission

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')  # URL to redirect after successful form submission

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category-list')  # URL to redirect after successful deletion

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response
    

class BrandListView(ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 5

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand_detail.html'

class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand_form.html'
    success_url = reverse_lazy('brand-list')  # URL to redirect after successful form submission

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand_form.html'
    success_url = reverse_lazy('brand-list')  # URL to redirect after successful form submission

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brand_confirm_delete.html'
    success_url = reverse_lazy('brand-list')  # URL to redirect after successful deletion

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response
    

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 5

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    paginate_by = 5

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    paginate_by = 5

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['customer', 'total_amount']
    success_url = reverse_lazy('order-list')

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['customer', 'total_amount']
    success_url = reverse_lazy('order-list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order-list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response

class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'orderitem_list.html'
    context_object_name = 'orderitems'
    paginate_by = 5

class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'orderitem_detail.html'

class OrderItemCreateView(CreateView):
    model = OrderItem
    template_name = 'orderitem_form.html'
    fields = ['order', 'product', 'quantity']
    success_url = reverse_lazy('orderitem-list')

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    template_name = 'orderitem_form.html'
    fields = ['order', 'product', 'quantity']
    success_url = reverse_lazy('orderitem-list')

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = 'orderitem_confirm_delete.html'
    success_url = reverse_lazy('orderitem-list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response
    
    





