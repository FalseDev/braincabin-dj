from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django_email_verification import urls as mail_urls
from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('confirm-mail/', views.confirm_mail, name="confirm-mail-message"),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/edit/', views.profile_edit, name="profile-edit"),
    path('password/', include('users.urls.password_urls')),
    path('email/', include(mail_urls)),
]
