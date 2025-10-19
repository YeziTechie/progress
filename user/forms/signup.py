import re

from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'desc-input', 'placeholder': 'Enter password'}),
        min_length=8
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'desc-input', 'placeholder': 'Confirm password'}),
        min_length=8
    )

    class Meta:
        model = User
        fields = ('username', 'profile_picture', 'element', 'animal', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'desc-input',
            'placeholder': 'Enter your Username'
        })
        self.fields['profile_picture'].widget.attrs['class'] = 'desc-input'
        self.fields['animal'].widget.attrs['class'] = 'desc-input'
        self.fields['element'].widget.attrs.update({
            'class': 'desc-input',
            'placeholder': 'Choose wisely'
        })

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username is required.")
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        if not re.match(r'^[A-Za-z0-9-_]+$', username):
            err = "Username may contain only letters, numbers, hyphens, or underscores (no spaces)."
            raise forms.ValidationError(err)
        return username
