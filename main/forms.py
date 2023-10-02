from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content']

        widgets = {
            "name": forms.HiddenInput(),
            "content": Textarea(attrs={
                'class': 'primary-input',
                'placeholder': 'Твоя мечта'
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content')

        widgets = {
            "name": forms.HiddenInput(),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
        }


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Твое Имя', 'class': 'primary-input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Твой Ник', 'class': 'primary-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'primary-input'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Повтори Пароль', 'class': 'primary-input'}))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Твой Ник', 'class': 'primary-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'primary-input'}))

    class Meta:
        fields = ('username', 'password')
