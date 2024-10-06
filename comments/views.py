from django.shortcuts import render


def comment_page(request):
    # Pass 'page' as 'comments' to indicate the active page
    context = {
        'page': 'comments',  # Add this to distinguish the page
    }
    return render(request, 'comments/comments.html', context)
