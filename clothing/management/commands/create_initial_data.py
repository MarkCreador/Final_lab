# yourapp/management/commands/populate_store.py

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from clothing.models import Category, Brand, Product, Customer, Order, OrderItem
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Populate the clothing store database with sample data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating the store database...'))

        # Create categories
        categories = ['Shirts', 'Pants', 'Shoes', 'Accessories']
        for category_name in categories:
            Category.objects.create(name=category_name)

        # Create brands
        brands = ['Nike', 'Adidas', 'Gucci', 'Zara', 'Levi\'s']
        for brand_name in brands:
            Brand.objects.create(name=brand_name)

        # Create products
        for _ in range(10):
            category = random.choice(Category.objects.all())
            brand = random.choice(Brand.objects.all())
            Product.objects.create(
                name=get_random_string(10),
                description=get_random_string(50),
                price=Decimal(random.uniform(10, 1000)),
                category=category,
            ).brands.add(brand)

        # Create customers
        for _ in range(5):
            Customer.objects.create(
                name=get_random_string(10),
                email=f'{get_random_string(10)}@example.com'
            )

        # Create orders
        for customer in Customer.objects.all():
            order = Order.objects.create(customer=customer, total_amount=Decimal(0))
            products = random.sample(list(Product.objects.all()), k=random.randint(1, 5))
            for product in products:
                quantity = random.randint(1, 10)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)
                order.total_amount += product.price * quantity
            order.save()

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))