from graphene_django import DjangoObjectType
from forum.models import Question, Answer
from users.models import Profile, User
from graphene import List, Int, Field
from django.db.models import Count


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("text", "question", "answered_by",
                  "answered_on", "accepted")

    score = Int()

    resolve_score = lambda self, _: self.get_score()

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("user", "status", "institute")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "title", "description", "asked_by",
                  "asked_on")
    answers = Field(List(AnswerType), offset=Int(required=False), limit=Int(required=False))

    def resolve_answers(self, info, offset=0, limit=10):
        return self.answer_set.annotate(score=Count("upvotes")-Count("downvotes")).order_by("-score")[offset:offset+limit]


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("username", "name", "join_date", "profile")

    top_questions = List(QuestionType)
    top_answers = List(AnswerType)
    reputation = Int()

    def resolve_top_questions(self, _): return self.top_questions()

    def resolve_top_answers(self, _): return self.top_answers()

    def resolve_reputation(self, _): return self.reputation()
