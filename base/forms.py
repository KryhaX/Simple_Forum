from django import forms
from django.forms import ModelForm

from .models import Logowanie, Czat

# Logowanie
class LogowanieForm(ModelForm):
    class Meta:
        model = Logowanie
        fields = ['nazwa_uzytkownika', 'haslo']


#  Czat
class CzatForm(ModelForm):
    class Meta:
        model = Czat
        fields = ['czat']