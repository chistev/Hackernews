from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('', views.comment_page, name='comment_page'),  # Renders the comment page
]
