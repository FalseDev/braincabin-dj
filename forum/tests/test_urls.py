from django.test import SimpleTestCase
from django.urls import resolve, reverse
from forum import views as forum_views
from forum import views

class TestForumUrls(SimpleTestCase):

    def test_questions_url_resolves(self):
        url = reverse('forum-questions')
        view = resolve(url)

        self.assertEqual(view.func.view_class, forum_views.QuestionListView)

    def test_question_url_resolves(self):
        url = reverse('question-detail', args=[2])
        view = resolve(url)

        self.assertEqual(view.func.view_class, forum_views.QuestionDetailView)

    def test_question_create_url_resolves(self):
        url = reverse('question-create')
        view = resolve(url)

        self.assertEqual(view.func.view_class, forum_views.QuestionCreateView)

    def test_answer_create_url_resolves(self):
        url = reverse('answer-create', args=[1])
        view = resolve(url)

        self.assertEqual(view.func, views.create_answer)