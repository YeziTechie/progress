import re

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'desc-input', 'placeholder': 'Enter your Username'}),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'desc-input', 'placeholder': 'Enter password'}),
        min_length=8
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username is required.")
        if not re.match(r'^[A-Za-z0-9-_]+$', username):
            raise forms.ValidationError("Invalid username format.")
        return username
