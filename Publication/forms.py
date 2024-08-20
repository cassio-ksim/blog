from django import forms
from .models import Publication, Author
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'content', 'date_publication')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PublicationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super(Author, self).save(commit=False)
        post.author = self.request.user
        if commit:
            post.save()
        return post


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=255)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')