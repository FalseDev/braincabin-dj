from django import forms
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(
        required=True, help_text="This is stored private", widget=forms.SelectDateWidget(years=range(1920, 2012)))

    class Meta:
        model = User
        fields = ['username', 'name', 'email',
                  'password1', 'password2', 'date_of_birth']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['status', 'institute']