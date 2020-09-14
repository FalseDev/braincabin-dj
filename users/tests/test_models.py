from django.test import TestCase
from users.models import User, Profile


class test_user_model(TestCase):

    def setUp(self):
        self.test_user1 = User.objects.create_user(
            name="TestUser", password="TestUserPassword", email="TestUser@mail.com",
            username="TestUserName", date_of_birth='2004-11-13')

        self.test_user2 = User.objects.create_user(
            name="TestUser", password="TestUser2Password", email="TestUser2@mail.com",
            username="TestUserName2", date_of_birth='2004-11-13')

    def test_profile_autocreation_for_user(self):
        self.assertEqual(
            len(Profile.objects.filter(user=self.test_user1)), 1)

    def test_profile_duplicate_creation_for_user(self):
        self.test_user2.name = "TestUserUpdatedName"
        self.test_user2.save()

        self.assertEqual(
            len(Profile.objects.filter(user=self.test_user2)), 1)
