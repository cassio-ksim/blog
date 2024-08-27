from django import forms
from .models import Publication, Comment
from django.contrib.auth.forms import UserCreationForm


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


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=4000)

    def save(self, post, commit=True):
        comment = Comment(post=post, text=self.cleaned_data['text'])
        if commit:
            comment.save()
        return comment