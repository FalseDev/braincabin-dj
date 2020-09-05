from forum.models import Question, User, Profile, Answer
from django.contrib.auth import hashers

def resolve_register(root, info, name, username, email, password):
    return User.objects.create(name=name, username=username,
                       email=email, password=hashers.make_password(password))


def resolve_login(root, info, username, password):
    user = User.objects.get(username=username)
    if hashers.check_password(password, user.password):
        info.context.session['F_LOGIN'] = user.username
        return user
    return None

def resolve_question(root, info, id):
    return Question.objects.get(id=id)


def resolve_user(root, info, id):
    return User.objects.get(id=id)


def resolve_all_questions(root, info, page=1, quantity=5):
    return Question.objects.all()[(page-1)*quantity:page*quantity]


def resolve_all_profiles(root, info, page=1, quantity=5):
    return Profile.objects.all()[(page-1)*quantity:page*quantity]
