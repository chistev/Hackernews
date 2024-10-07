from django.urls import path
from . import views

app_name = 'ask'

urlpatterns = [
    path('', views.ask_page, name='ask_page'),
]
