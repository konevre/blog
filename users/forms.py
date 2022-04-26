from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Profile
from django.utils.translation import gettext_lazy as _


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=64)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('email', )


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', ]
