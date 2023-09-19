from django.db import models

class Logowanie(models.Model):
    nazwa_uzytkownika = models.CharField(max_length=12, blank=False, unique=True)
    haslo = models.CharField(max_length=12, blank=False, unique=True)

    def __str__(self):
        return self.login_haslo()

    def login_haslo(self):
        return "L: {} H: ({})".format(self.nazwa_uzytkownika, self.haslo)

class Pokoj(models.Model):
    tytul = models.CharField(max_length=70)
    opis = models.TextField(null=True,blank=True)
    aktualizacja = models.DateTimeField(auto_now=True)
    stworzono = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tytul