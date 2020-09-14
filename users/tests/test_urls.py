from django.test import SimpleTestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from users import views


class TestAccountAuthUrls(SimpleTestCase):
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, views.register)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)


class TestPasswordActionUrls(SimpleTestCase):
    def test_password_reset_url_resolves(self):
        url = reverse('password_reset')
        self.assertEqual(resolve(url).func.view_class, PasswordResetView)

    def test_password_reset_done_url_resolves(self):
        url = reverse('password_reset_done')
        self.assertEqual(resolve(url).func.view_class, PasswordResetDoneView)

    def test_password_reset_confirm_url_resolves(self):
        url = reverse('password_reset_confirm', args=['uidb64', 'token'])
        self.assertEqual(resolve(url).func.view_class,
                         PasswordResetConfirmView)

    def test_password_reset_complete_url_resolves(self):
        url = reverse('password_reset_complete')
        self.assertEqual(resolve(url).func.view_class,
                         PasswordResetCompleteView)

    def test_password_change_url_resolves(self):
        url = reverse('password_change')
        self.assertEqual(resolve(url).func.view_class, PasswordChangeView)

    def test_password_change_done_url_resolves(self):
        url = reverse('password_change_done')
        self.assertEqual(resolve(url).func.view_class, PasswordChangeDoneView)
