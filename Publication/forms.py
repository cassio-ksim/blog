from django import forms
from .models import Publication, Author
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'content',)  # Campos do formulário

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=255)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')