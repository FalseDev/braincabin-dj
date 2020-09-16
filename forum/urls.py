from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.QuestionListView.as_view(), name='forum-questions'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('question/ask/', views.QuestionCreateView.as_view(), name='question-create'),
    path('answer/<int:question_id>/', views.create_answer, name="answer-create"),
]
