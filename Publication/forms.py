from django import forms
from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'content', 'author')  # Campos que você deseja incluir no formulário