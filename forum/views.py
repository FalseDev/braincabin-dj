from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import Textarea
from django.contrib import messages
from .models import Question, Answer
from . import forms


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
            "placeholder": "Explain your question here!",
        })
        return form

    def form_valid(self, form):
        form.instance.asked_by = self.request.user
        return super().form_valid(form)


def create_answer(request, question_id):
    if request.method == 'POST':
        form = forms.AnswerCreationForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data['text']
            answered_by = request.user
            try:
                Answer.objects.create(
                    text=text, question_id=question_id, answered_by=answered_by)
            except:
                return Http404
            messages.success(request, 'Answer added!')
            return redirect('question-detail', pk=question_id)
    else:
        form = forms.AnswerCreationForm()
        question = get_object_or_404(Question, id=question_id)
    return render(request, 'forum/answer.html', {"form": form, "question": question})


def vote(request, model_type, vote_type, action_type, pk):
    if request.method != 'POST':
        return JsonResponse({"success": False})

    if request.user.is_anonymous:
        return JsonResponse({"success": False})

    if model_type == 'question':
        model = Question
    elif model_type == 'answer':
        model = Answer
    else:
        return Http404()

    op_object = get_object_or_404(model, pk=pk)

    if vote_type == 'upvote':
        vote_obj = op_object.downvotes
        unvote_obj = op_object.upvotes
    elif vote_type == 'downvote':
        vote_obj = op_object.downvotes
        unvote_obj = op_object.upvotes
    else:
        return Http404()

    if action_type == 'add':
        unvote_obj.remove(request.user)
        vote_obj.add(request.user)
    elif action_type == 'remove':
        vote_obj.remove(requst.user)
    else:
        return Http404()

    return JsonResponse({"success": True})
