from django.contrib import admin
from .models import Answer, Question, AnswerVote, QuestionVote

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(AnswerVote)
admin.site.register(QuestionVote)
