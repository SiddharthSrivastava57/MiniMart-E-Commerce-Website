# shop/admin.py

from django.contrib import admin
from .models import Category, Product, Wishlist

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing categories
    """
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for managing products
    Shows key fields in list view and allows filtering/searching
    """
    list_display = ('name', 'category', 'price', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    list_per_page = 20


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """
    Admin can see all wishlist items
    Useful for debugging or analytics
    """
    list_display = ('user', 'product', 'added_at')
    list_filter = ('user', 'added_at')
    search_fields = ('user__username', 'product__name')