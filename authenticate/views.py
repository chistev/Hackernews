from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home:home')  # Redirect to a home page or wherever you want
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'authenticate/login.html')

    return render(request, 'authenticate/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('new-username')
        password = request.POST.get('new-password')

        # Validate username and password length
        if len(username) < 3 or len(password) < 6:
            messages.error(request, "Username must be at least 3 characters and password at least 6 characters long.")
            return render(request, 'authenticate/login.html')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'authenticate/login.html')

        # Create the user and log them in
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect('home:home')  # Redirect to a home page or wherever you want

    return render(request, 'authenticate/register.html')


def logout_view(request):
    logout(request)
    return redirect('home:home')


def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST.get('s')

        # Check if a user exists with the provided email
        if User.objects.filter(username=email).exists():
            # User exists, you can redirect them to a different page or render a success message
            messages.success(request, "A password reset link has been sent to your email.")
            return redirect('home:home')  # Change to your desired redirect URL
        else:
            # User does not exist, redirect to a specific page
            messages.error(request, "No user found with that email address.")
            return redirect('authenticate:not_found')  # Change to your desired redirect URL for not found

    return render(request, 'authenticate/password_reset.html')


def not_found_view(request):
    return render(request, 'authenticate/not_found.html')
