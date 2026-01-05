# shop/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from shop.models import Category, Product

class Command(BaseCommand):
    help = 'Populate database with sample products'

    def handle(self, *args, **kwargs):
        # Create categories
        electronics = Category.objects.get_or_create(name='Electronics')[0]
        books = Category.objects.get_or_create(name='Books')[0]
        clothing = Category.objects.get_or_create(name='Clothing')[0]
        home = Category.objects.get_or_create(name='Home & Kitchen')[0]

        # Create products
        products = [
            Product(name='Wireless Mouse', description='Ergonomic wireless mouse with USB receiver', price=29.99, category=electronics),
            Product(name='Python Programming Book', description='Learn Python from scratch', price=39.99, category=books),
            Product(name='Cotton T-Shirt', description='Comfortable cotton t-shirt', price=19.99, category=clothing),
            Product(name='Coffee Maker', description='Automatic drip coffee maker', price=79.99, category=home),
            Product(name='Laptop Stand', description='Aluminum adjustable laptop stand', price=49.99, category=electronics),
            Product(name='Django Cookbook', description='Advanced Django recipes', price=44.99, category=books),
            Product(name='Running Shoes', description='Lightweight running shoes', price=89.99, category=clothing),
            Product(name='Blender', description='High-speed kitchen blender', price=99.99, category=home),
        ]

        Product.objects.bulk_create(products, ignore_conflicts=True)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database!'))