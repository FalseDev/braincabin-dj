from django.contrib.auth import authenticate, login, logout
from forum.models import Question, Answer
from users.models import Profile
from users.models import User


def resolve_register(root, info, name, username, email, password):
    return User.objects.create_user(username, email=email, password=password, name=name)


def resolve_login(root, info, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(info.context, user)
    return user


def resolve_logout(root, info):
    logout(info.context)


def resolve_question(root, info, id):
    return Question.objects.get(id=id)


def resolve_user(root, info, id):
    return User.objects.get(id=id)


def resolve_all_questions(root, info, page=1, quantity=5):
    return Question.objects.all()[(page-1)*quantity:page*quantity]


def resolve_all_profiles(root, info, page=1, quantity=5):
    return Profile.objects.all()[(page-1)*quantity:page*quantity]
