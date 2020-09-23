from graphene_django import DjangoObjectType
from forum.models import Question, Answer
from users.models import Profile, User
from graphene import List


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("text", "question", "answered_by",
                  "answered_on")


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("user", "status", "institute")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "title", "description", "asked_by",
                  "asked_on")
    answers = List(AnswerType)
    def resolve_answers(self,info):
       return self.answer_set.all()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("username", "name", "reputation", "join_date", "profile")

    top_questions = List(QuestionType)
    top_answers = List(AnswerType)

    def resolve_top_questions(self, info):
        return self.question_set.filter(asked_by=info.context.user)[:5]

    def resolve_top_answers(self, info):
        return self.answer_set.filter(answered_by=info.context.user)[:5]
