from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.questions, name='forum-questions'),
]
