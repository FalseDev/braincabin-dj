from django.db import models


class User(models.Model):
    username = models.CharField('Unique username', max_length=20, unique=True)
    name = models.CharField('User\'s name', max_length=30)

    password = models.CharField('Hashed password', max_length=78)
    email = models.EmailField('Email of the user', unique=True)

    reputation = models.IntegerField('Reputation of user', default=0)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    SCHOOLER = "SCHOOLER"
    UNDERGRAD = "UNDERGRAD"
    GRADUATE = "GRADUATE"
    OTHER = "OTHER"

    status_choices = [
        (SCHOOLER, "SCH"),
        (UNDERGRAD, "UGD"),
        (GRADUATE, "GDE"),
        (OTHER, "OTH"),
    ]

    status = models.CharField(choices=status_choices,max_length=9)
    institute = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user.username}'s profile"

class Question(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    asked_by = models.ForeignKey('User', on_delete=models.CASCADE)

    answer_count = models.IntegerField(default=0)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Answer(models.Model):
    answered_by = models.ForeignKey('User', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField('The answer itself', max_length=2000)

    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text[0:10]}{'...' if len(self.text)>10 else ''}"


class AnswerVote(models.Model):
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    upvotes = models.ManyToManyField('User', related_name='ans_upvote',blank=True)
    downvotes = models.ManyToManyField('User', related_name='ans_downvote',blank=True)


class QuestionVote(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    upvotes = models.ManyToManyField('User', related_name='que_upvote',blank=True)
    downvotes = models.ManyToManyField('User', related_name='que_downvote',blank=True)
