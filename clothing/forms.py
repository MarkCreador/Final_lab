from django import forms
from .models import Category, Brand, Product, Customer, Order, OrderItem

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'brands']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

class OrderForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all())
    total_amount = forms.DecimalField()

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']


