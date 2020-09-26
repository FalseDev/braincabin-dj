from django.contrib.auth import authenticate, login, logout
from forum.models import Question, Answer
from users.models import Profile
from users.models import User


def resolve_register(root, info, name, username, email, password, date_of_birth):
    if (User.objects.filter(username=username)):
        return None
    if (User.objects.filter(email=email)):
        return None
    return User.objects.create_user(username, email=email, password=password, name=name, date_of_birth=date_of_birth)


def resolve_login(root, info, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(info.context, user)
    return user


def resolve_logout(root, info):
    logout(info.context)


def resolve_question(root, info, id):
    question = Question.objects.filter(id=id)
    if question:
        return question[0]
    return None


def resolve_user(root, info, id):
    user = User.objects.filter(id=id)
    if(user):
        return user[0]
    return None


def resolve_all_questions(root, info, limit=10, offset=0):
    return Question.objects.all()[offset:offset+limit]


def resolve_users(root, info, limit=10, offset=0):
    return User.objects.all()[offset:offset+limit]
