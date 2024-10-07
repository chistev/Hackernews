from django.shortcuts import render

def jobs_page(request):
    context = {
        'page': 'jobs',  # Add this to distinguish the page
    }
    return render(request, 'jobs/jobs.html', context)
