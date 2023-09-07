from django.db import models


class Logowanie(models.Model):
    nazwa_uzytkownika = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=20, blank=False, null=False)
    haslo = models.CharField(max_length=28, blank=False, null=False)
