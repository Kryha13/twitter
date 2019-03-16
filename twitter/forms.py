from django.contrib.auth.forms import UserCreationForm

from twitter.models import User, Tweet
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TweetFrom(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Tweet
        fields = ['content']

