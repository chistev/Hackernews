from django.urls import path
from .views import login_view

app_name = 'authenticate'

urlpatterns = [
    path('login/', login_view, name='login'),
]
