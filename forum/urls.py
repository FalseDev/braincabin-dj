from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('questions/', views.QuestionListView.as_view(), name='forum-questions'),
    path('question/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('question/ask/', views.create_question, name='question-create'),
    path('answer/<int:question_id>/', views.create_answer, name="answer-create"),

    path('tags/create/', views.RequestNewTag.as_view(), name="new-tag"),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name="tagged-question"),

    path('answer/accept/<int:question_pk>/<int:answer_pk>/',
         csrf_exempt(views.accept_answer), name="answer-accept"),
    path('vote/<str:model_type>/<str:vote_type>/<str:action_type>/<int:pk>/',
         csrf_exempt(views.vote), name="forum_vote"),

    path('questiontags.json', views.question_tags_json, name="questiontags-json"),
]
