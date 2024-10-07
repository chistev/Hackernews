from django.shortcuts import render

def show_page(request):
    context = {
        'page': 'show',  # Add this to distinguish the page
    }
    return render(request, 'show/show.html', context)
