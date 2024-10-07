from django.shortcuts import render

def ask_page(request):
    context = {
        'page': 'ask',  # Add this to distinguish the page
    }
    return render(request, 'ask/ask.html', context)
