from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home'),  # Home page, default view
    path('newest/', views.newest_page, name='newest'),  # Newest posts view

    # Date-based views
    path('past/', views.past_posts, name='past'),  # Default: current date posts
    path('past/<int:days_ago>/', views.past_posts, name='past_with_days'),  # Filter posts from a specific day ago
    path('next_day/<int:days_ago>/', views.next_day_posts, name='next_day'),  # Show posts for the next day with days_ago
]
