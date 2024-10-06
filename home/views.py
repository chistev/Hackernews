from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Post

def home_page(request):
    posts = Post.objects.all()  # Get all posts
    context = {
        'posts': posts,
        'page': 'home',  # Add this to distinguish the page
    }
    return render(request, 'home/index.html', context)


def newest_page(request):
    posts = Post.objects.all().order_by('-created_at')  # Order by created_at descending
    context = {
        'posts': posts,
        'page': 'newest',  # Add this to distinguish the page
    }
    return render(request, 'home/index.html', context)


def past_posts(request, days_ago=1):
    # Calculate the target date based on the `days_ago` parameter
    target_date = timezone.now() - timedelta(days=days_ago)

    # Query the posts created on the specific date (target_date)
    posts = Post.objects.filter(created_at__date=target_date.date()).order_by('-created_at')

    context = {
        'posts': posts,
        'page': 'past',  # Add 'past' to distinguish the page
        'current_date': target_date.strftime("%Y-%m-%d"),  # Pass the current date for the view
        'days_ago': days_ago,  # Pass days_ago to the template for further navigation
    }
    return render(request, 'home/index.html', context)


def next_day_posts(request, days_ago=1):
    # Calculate the target date based on the `days_ago` parameter
    target_date = timezone.now() - timedelta(days=days_ago) + timedelta(days=1)

    # Query the posts created on the next day's date
    posts = Post.objects.filter(created_at__date=target_date.date()).order_by('-created_at')

    context = {
        'posts': posts,
        'page': 'past',  # Keep the page as 'past'
        'current_date': target_date.strftime("%Y-%m-%d"),
        'days_ago': days_ago,  # Pass days_ago to the template for further navigation
    }
    return render(request, 'home/index.html', context)
