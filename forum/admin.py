from django.contrib import admin
from .models import User, Profile, Answer, Question, AnswerVote, QuestionVote

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(AnswerVote)
admin.site.register(QuestionVote)
