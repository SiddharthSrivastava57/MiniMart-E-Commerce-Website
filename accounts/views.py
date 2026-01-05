# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup_view(request):
    """
    User registration view
    Uses Django's built-in UserCreationForm
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('product_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    """
    Simple logout view
    """
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('product_list')