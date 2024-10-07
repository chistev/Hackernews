from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import timedelta

from django.views.decorators.http import require_POST

from .models import Post, HiddenPost


def home_page(request):
    posts = Post.objects.all()  # Get all posts

    if request.user.is_authenticated:
        hidden_posts = HiddenPost.objects.filter(user=request.user).values_list('post_id', flat=True)
        posts = posts.exclude(id__in=hidden_posts)  # Exclude hidden posts for the logged-in user

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


def posts_by_domain(request, domain):
    posts = Post.objects.filter(url__icontains=domain).order_by('-created_at')
    context = {
        'posts': posts,
        'page': 'domain',  # You can set this to distinguish the page
        'domain': domain,  # Pass the domain to the template if needed
    }
    return render(request, 'home/posts_by_domain.html', context)


@login_required  # Ensure only logged-in users can upvote
@require_POST
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    post.upvote(user)

    # Return the updated points as HTML
    post_html = render_to_string('home/points_snippet.html', {'post': post})
    return HttpResponse(post_html)

def author_details(request, author_id):
    author = get_object_or_404(User, id=author_id)
    posts = Post.objects.filter(author=author).order_by('-created_at')  # Get posts by this author

    context = {
        'author': author,
        'posts': posts,
    }
    return render(request, 'home/author_details.html', context)


@login_required
@require_POST
def hide_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    HiddenPost.objects.get_or_create(user=request.user, post=post)

    # Fetch all remaining posts for the current page
    remaining_posts = Post.objects.exclude(hiddenpost__user=request.user).order_by('-created_at')

    # Render the updated posts list
    return render(request, 'home/hidden_post.html', {'posts': remaining_posts, 'page': 'home'})
