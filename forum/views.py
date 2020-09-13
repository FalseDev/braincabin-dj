from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import Textarea
from .models import Question

class QuestionListView(ListView):
    model = Question
    template_name = 'forum/questions.html'
    context_object_name = 'questions'
    paginate_by = 5
    ordering = '-asked_on'

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'description']

    def get_form(self, form_class=None):
        form = super(QuestionCreateView, self).get_form(form_class=form_class)
        form.fields['description'].widget = Textarea({
            "placeholder":"Explain your question here!",
            })
        return form

    def form_valid(self,form):
        form.instance.asked_by = self.request.user
        return super().form_valid(form)