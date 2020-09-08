from django.db import models
from users.models import User


class Question(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    answer_count = models.IntegerField(default=0)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Answer(models.Model):
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField('The answer itself', max_length=2000)

    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text[0:10]}{'...' if len(self.text)>10 else ''}"


class AnswerVote(models.Model):
    answer = models.OneToOneField('Answer', on_delete=models.CASCADE)
    upvotes = models.ManyToManyField(
        User, related_name='ans_upvote', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='ans_downvote', blank=True)


class QuestionVote(models.Model):
    question = models.OneToOneField('Question', on_delete=models.CASCADE)
    upvotes = models.ManyToManyField(
        User, related_name='que_upvote', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='que_downvote', blank=True)
