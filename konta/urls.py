from django.urls import path

# Logowanie i Rejestracja
from konta.views import logowanie

urlpatterns = [
    path('logowanie/', logowanie, name="logowanie"),

]
