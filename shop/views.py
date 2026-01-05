# shop/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Wishlist, Category

def product_list(request):
    """
    Main view: Display all products with sorting
    This view handles both initial page load and HTMX sorting requests
    """
    # Get sort parameter from URL (?sort=price_low)
    sort_by = request.GET.get('sort', 'name')
    
    # Apply sorting based on parameter
    if sort_by == 'price_low':
        products = Product.objects.all().order_by('price')
    elif sort_by == 'price_high':
        products = Product.objects.all().order_by('-price')  # minus sign = descending
    else:
        products = Product.objects.all().order_by('name')
    
    # Get user's wishlist product IDs (if logged in)
    wishlist_product_ids = []
    if request.user.is_authenticated:
        wishlist_product_ids = Wishlist.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)
    
    context = {
        'products': products,
        'wishlist_product_ids': list(wishlist_product_ids),
        'current_sort': sort_by,
    }
    
    # HTMX sends a special header when making requests
    # If request is from HTMX, return only the product list partial
    # Otherwise, return the full page
    if request.headers.get('HX-Request'):
        return render(request, 'shop/partials/product_list_partial.html', context)
    
    return render(request, 'shop/product_list.html', context)


@login_required  # Decorator ensures only logged-in users can access this
def add_to_wishlist(request, product_id):
    """
    Add a product to user's wishlist
    Uses get_or_create to avoid duplicate entries
    """
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        
        # get_or_create returns (object, created_boolean)
        wishlist_item, created = Wishlist.objects.get_or_create(
            user=request.user,
            product=product
        )
        
        if created:
            messages.success(request, f'{product.name} added to wishlist!')
        else:
            messages.info(request, f'{product.name} is already in your wishlist.')
        
        # Return the updated button HTML for HTMX to swap
        context = {
            'product': product,
            'in_wishlist': True
        }
        return render(request, 'shop/partials/wishlist_button.html', context)
    
    return redirect('product_list')


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from user's wishlist
    """
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        
        # Delete the wishlist entry
        Wishlist.objects.filter(user=request.user, product=product).delete()
        
        messages.success(request, f'{product.name} removed from wishlist.')
        
        # Check if request is from wishlist page or product list
        # If from wishlist page, return empty (to remove the card)
        # If from product list, return updated button
        referer = request.headers.get('HX-Current-URL', '')
        
        if 'wishlist' in referer:
            # From wishlist page - return empty to remove the card
            return render(request, 'shop/partials/empty.html')
        else:
            # From product list - return updated button
            context = {
                'product': product,
                'in_wishlist': False
            }
            return render(request, 'shop/partials/wishlist_button.html', context)
    
    return redirect('product_list')


@login_required
def wishlist_view(request):
    """
    Display user's wishlist page
    """
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    
    context = {
        'wishlist_items': wishlist_items
    }
    return render(request, 'shop/wishlist.html', context)


# shop/views.py - Add this debugging version temporarily

@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to user's wishlist
    """
    print(f"=== ADD TO WISHLIST DEBUG ===")
    print(f"Method: {request.method}")
    print(f"User: {request.user}")
    print(f"Product ID: {product_id}")
    print(f"Is HTMX: {request.headers.get('HX-Request')}")
    
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        print(f"Product found: {product.name}")
        
        # get_or_create returns (object, created_boolean)
        wishlist_item, created = Wishlist.objects.get_or_create(
            user=request.user,
            product=product
        )
        
        print(f"Wishlist item created: {created}")
        
        if created:
            messages.success(request, f'{product.name} added to wishlist!')
        else:
            messages.info(request, f'{product.name} is already in your wishlist.')
        
        # Return the updated button HTML for HTMX to swap
        context = {
            'product': product,
            'in_wishlist': True
        }
        return render(request, 'shop/partials/wishlist_button.html', context)
    
    print("Not a POST request, redirecting...")
    return redirect('product_list')