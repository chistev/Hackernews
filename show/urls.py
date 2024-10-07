from django.urls import path
from . import views

app_name = 'show'

urlpatterns = [
    path('', views.show_page, name='show_page'),
]
