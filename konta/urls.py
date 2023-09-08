from django.urls import path

# Logowanie i Rejestracja
from konta.views import logowanie, moje_konto

urlpatterns = [
    path('logowanie/', logowanie, name="logowanie"),
    path('moje_konto/', moje_konto, name="moje_konto"),

]
