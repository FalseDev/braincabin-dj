from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Question

class QuestionListView(ListView):
    model = Question
    template_name = 'forum/questions.html'
    context_object_name = 'questions'

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'description']

    def form_valid(self,form):
        form.instance.asked_by = self.request.user
        return super().form_valid(form)