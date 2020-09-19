from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('questions/', views.QuestionListView.as_view(), name='forum-questions'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('question/ask/', views.QuestionCreateView.as_view(), name='question-create'),
    path('answer/<int:question_id>/', views.create_answer, name="answer-create"),
    path('vote/<str:model_type>/<str:vote_type>/<str:action_type>/<int:pk>/',
         csrf_exempt(views.vote), name="forum_vote"),
]
