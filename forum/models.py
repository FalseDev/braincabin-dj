from django.db import models
from users.models import User
from django.urls import reverse
from django_bleach.models import BleachField


class Question(models.Model):
    title = models.CharField(max_length=30)
    description = BleachField(max_length=2000)

    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    asked_on = models.DateField(auto_now_add=True)

    upvotes = models.ManyToManyField(
        User, related_name='ans_upvote', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='ans_downvote', blank=True)

    accepted_answer = models.OneToOneField('Answer', null=True, on_delete=models.CASCADE, related_name="accepted_for_question")

    def get_score(self):
        return self.upvotes.count() - self.downvotes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("question-detail", kwargs={"pk": self.pk})



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
        return self.upvotes.count() - self.downvotes.count()

    def __str__(self):
        return f"{self.text[0:10]}{'...' if len(self.text)>10 else ''}"
