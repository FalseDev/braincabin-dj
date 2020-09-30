from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.forms import Textarea
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from ckeditor.widgets import CKEditorWidget
import json
from .models import Question, Answer, QuestionTag
from . import forms


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    paginate_by = 5
    ordering = '-asked_on'


class QuestionDetailView(DetailView):
    model = Question


class RequestNewTag(LoginRequiredMixin, CreateView):
    model = QuestionTag
    fields = ['name', 'ref', 'description']


class TagDetailView(DetailView):
    model = QuestionTag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['object']

        try:
            page_number = int(self.request.GET['page'])
        except:
            page_number = 1

        paginator = Paginator(tag.questions.order_by('-asked_on'), 15)
        context['page_obj'] = paginator.get_page(page_number)
        context['is_paginated'] = tag.questions.count() > 15

        return context


def question_tags_json(request):
    tags = [{"value": tag.name, "ref": tag.ref}
            for tag in QuestionTag.objects.filter(active=True)]
    return JsonResponse({"tags": tags})


@login_required
def create_question(request):
    if request.method == 'POST':
        form = forms.QuestionCreationForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            title = form.cleaned_data['title']
            question = Question.objects.create(
                title=title, description=description,
                asked_by=request.user)
            try:
                tagObjects = json.loads(form.data['tags'])
            except:
                pass
            else:
                tags = [QuestionTag.objects.get(ref=tagref) for tagref in [
                    tag['ref'] for tag in tagObjects]]
                question.tags.set(tags)

            messages.success(request, 'Question asked!')
            return redirect('question-detail', pk=question.id)
    else:
        form = forms.QuestionCreationForm()
    return render(request, 'forum/question_form.html', {"form": form})


@login_required
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
    return render(request, 'forum/add_answer.html', {"form": form, "question": question})


def vote(request, model_type, vote_type, action_type, pk):
    if request.method != 'POST':
        return JsonResponse({"success": False, "errors": ["Invalid request method"]})

    if request.user.is_anonymous:
        return JsonResponse({"success": False, "errors": ["You're not logged in"]})

    if model_type == 'question':
        model = Question
    elif model_type == 'answer':
        model = Answer
    else:
        return JsonResponse({"success": True, "errors": ["Invalid model"]})

    try:
        op_object = model.objects.get(pk=pk)
    except:
        return JsonResponse({"success": False, "errors": ["Invalid object id"]})

    if (model == Question and op_object.asked_by == request.user) or (model == Answer and op_object.answered_by == request.user):
        return JsonResponse({"success": False, "errors": [f"You cannot {vote_type} your own {model_type}"]})

    if vote_type == 'downvote':
        vote_obj = op_object.downvotes
        unvote_obj = op_object.upvotes
    elif vote_type == 'upvote':
        unvote_obj = op_object.downvotes
        vote_obj = op_object.upvotes
    else:
        return JsonResponse({"success": False, "errors": ["Invalid vote type"]})

    if action_type == 'add':
        if unvote_obj.filter(pk=request.user.pk):
            unvote_obj.remove(request.user)

        if not vote_obj.filter(pk=request.user.pk):
            vote_obj.add(request.user)
        else:
            return JsonResponse({"success": False})

    elif action_type == 'remove':
        unvote_obj.remove(request.user)
        vote_obj.remove(request.user)
    else:
        return JsonResponse({"success": False, "errors": ["Invalid action type"]})

    return JsonResponse({"success": True})


def accept_answer(request, question_pk, answer_pk):
    try:
        question = Question.objects.get(pk=question_pk)
    except:
        return HttpResponseBadRequest()

    try:
        answer = question.answer_set.get(pk=answer_pk)
    except:
        return HttpResponseBadRequest()

    if request.user != question.asked_by:
        return HttpResponseNotAllowed('GET')

    if request.method != "POST":
        return HttpResponseBadRequest()

    if question.accepted_answer:
        return JsonResponse({
            "success": False,
            "errors": ["You've already accepted an answer"]
        })

    if answer.answered_by == request.user:
        return JsonResponse({
            "success": False,
            "errors": ["You cannot accept your own answer"]
        })

    question.accepted_answer = answer
    question.save()

    return JsonResponse({"success": True})
