from django import forms
from django.forms import ModelForm

# Logowanie i Rejestracja
from .models import Logowanie#, Rejestracja

# Logowanie
class LogowanieForm(ModelForm):
    class Meta:
        model = Logowanie
        fields = ['nazwa_uzytkownika', 'haslo', 'email']

# Rejestracja
# class RejestracjaForm(ModelForm):
#     class Meta:
#         model = Rejestracja
#         fields = ['nazwa_uzytkownika', 'haslo', 'email']