from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.jobs_page, name='jobs_page'),
]
