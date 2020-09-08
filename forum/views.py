from django.shortcuts import render
from .models import Question
def questions(request):
    questions = Question.objects.order_by('id')[:5]
    return render(request, 'forum/questions.html',{'questions':questions})