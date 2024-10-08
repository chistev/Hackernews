from django.urls import path
from .views import login_view, register_view, logout_view, password_reset_view, not_found_view

app_name = 'authenticate'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('not-found/', not_found_view, name='not_found'),
]
