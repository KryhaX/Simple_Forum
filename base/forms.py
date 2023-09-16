from django import forms
from django.forms import ModelForm

# Logowanie i Rejestracja
from .models import Logowanie

# Logowanie
class LogowanieForm(ModelForm):
    class Meta:
        model = Logowanie
        fields = ['nazwa_uzytkownika', 'haslo']


