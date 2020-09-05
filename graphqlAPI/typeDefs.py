from graphene_django import DjangoObjectType
from forum.models import Question, User, Profile, Answer


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
        fields = ("username", "name", "reputation", "join_date")
