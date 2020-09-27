from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models import Count


class User(AbstractUser):
    name = models.CharField(max_length=30)

    join_date = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField()

    REQUIRED_FIELDS = ['date_of_birth', 'name', 'email']

    def reputation(self):
        questions = self.question_set.annotate(score=(Count('upvotes')-(2 * Count('downvotes'))))
        answers = self.answer_set.annotate(score=(Count('upvotes')-(2 * Count('downvotes'))))
        question_score = sum([q.score for q in questions])
        answer_score = sum([q.score for q in answers])
        accepted_answers_score = self.answer_set.exclude(accepted_for_question=None).count() * 15
        return answer_score + question_score + accepted_answers_score
    
    def top_questions(self, amount=5):
        return self.question_set.annotate(score=(Count('upvotes')-(2 * Count('downvotes')))).order_by('-score')[:amount]

    def top_answers(self, amount=5):
        return self.answer_set.annotate(score=(Count('upvotes')-(2 * Count('downvotes')))).order_by('-score')[:amount]

    def get_absolute_url(self):
        return reverse("user-detail", kwargs={"pk": self.pk})
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    SCHOOLER = "SCHOOLER"
    UNDERGRAD = "UNDERGRAD"
    GRADUATE = "GRADUATE"
    TEACHER = "TEACHER"
    OTHER = "OTHER"

    status_choices = [
        (SCHOOLER, SCHOOLER.capitalize()),
        (UNDERGRAD, UNDERGRAD.capitalize()),
        (GRADUATE, GRADUATE.capitalize()),
        (TEACHER, TEACHER.capitalize()),
        (OTHER, OTHER.capitalize()),
    ]

    status = models.CharField(choices=status_choices, max_length=9, null=True, blank=True)
    institute = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
