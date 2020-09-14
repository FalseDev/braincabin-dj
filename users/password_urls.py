from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [

    path('reset/', PasswordResetView.as_view(
        template_name="users/password/reset.html"), name="password_reset"),

    path('reset/done/', PasswordResetDoneView.as_view(
        template_name="users/password/reset_done.html"), name="password_reset_done"),

    path('reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="users/password/reset_confirm.html"), name="password_reset_confirm"),

    path('reset/complete/', PasswordResetCompleteView.as_view(
        template_name="users/password/reset_complete.html"), name="password_reset_complete"),

    path('change/', PasswordChangeView.as_view(
        template_name="users/password/change.html"), name="password_change"),

    path('change/done/', PasswordChangeDoneView.as_view(
        template_name="users/password/change_done.html"), name="password_change_done"),

]
