from django.shortcuts import render
from .models import Post


def home_page(request):
    # Fetch all posts from the database
    posts = Post.objects.all()  # Get all posts
    context = {
        'posts': posts,
        'page': 'home',  # Add this to distinguish the page
    }
    return render(request, 'home/index.html', context)


def newest_page(request):
    # Fetch the newest posts, ordered by creation date (most recent first)
    posts = Post.objects.all().order_by('-created_at')  # Order by created_at descending
    context = {
        'posts': posts,
        'page': 'newest',  # Add this to distinguish the page
    }
    return render(request, 'home/index.html', context)
