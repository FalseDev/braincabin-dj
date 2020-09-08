from graphene_django import DjangoObjectType
from forum.models import Question, Answer
from users.models import Profile, User
from graphene import List


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("text", "question", "answered_by",
                  "upvote_count", "downvote_count")


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("user", "status", "institute")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "title", "description", "upvote_count",
                  "downvote_count", "answer_count", "asked_by")


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("username", "name", "reputation", "join_date", "profile")

    top_questions = List(QuestionType)
    top_answers = List(AnswerType)

    def resolve_top_questions(self, info):
        return self.question_set.order_by('upvote_count')[:5]

    def resolve_top_answers(self, info):
        return self.answer_set.order_by('upvote_count')[:5]
