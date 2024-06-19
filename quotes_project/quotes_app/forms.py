from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Author, Quote

class TagSearchForm(forms.Form):
    tags = forms.CharField(max_length=100)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "bio"]

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["text", "author"]