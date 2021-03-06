from django.db import models
from users.models import User
from django.urls import reverse
from django_bleach.models import BleachField


class Question(models.Model):
    title = models.CharField(max_length=50)
    description = BleachField(max_length=2000)

    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    asked_on = models.DateField(auto_now_add=True)

    upvotes = models.ManyToManyField(
        User, related_name='ans_upvote', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='ans_downvote', blank=True)

    accepted_answer = models.OneToOneField(
        'Answer', null=True, on_delete=models.CASCADE, related_name="accepted_for_question", blank=True)
    tags = models.ManyToManyField(
        'QuestionTag', blank=True, related_name='questions')

    def get_score(self):
        return self.upvotes.count() - (2 * self.downvotes.count())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("question-detail", kwargs={"pk": self.pk})


class QuestionTag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(
        max_length=200, help_text="A brief discription of the tag")
    ref = models.IntegerField(
        unique=True, help_text="A unique reference number")
    active = models.BooleanField(default=False)

    def activate(self):
        self.active = True
        self.save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tagged-question", kwargs={"pk": self.pk})


class Answer(models.Model):
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answered_on = models.DateField(auto_now_add=True)

    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = BleachField('The answer itself', max_length=2000)

    upvotes = models.ManyToManyField(
        User, related_name='que_upvote', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='que_downvote', blank=True)

    def get_score(self):
        return self.upvotes.count() - (2 * self.downvotes.count())

    def __str__(self):
        return f"{self.text[0:10]}{'...' if len(self.text)>10 else ''}"

    def get_absolute_url(self):
        return reverse("question-detail", kwargs={"pk": self.question.pk}) + f'#answer{self.pk}'
