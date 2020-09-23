from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=30)

    reputation = models.IntegerField('Reputation of user', default=0)
    join_date = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField()

    REQUIRED_FIELDS = ['date_of_birth', 'name', 'email']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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

    status = models.CharField(choices=status_choices, max_length=9, null=True)
    institute = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
