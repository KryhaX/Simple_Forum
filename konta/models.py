from django.db import models

# class Moje_konto(models.Model):
#     nazwa_uzytkownika = models.CharField(max_length=15, blank=False, null=False)
#     email = models.CharField(max_length=20, blank=False, null=False)
#     haslo = models.CharField(max_length=28, blank=False, null=False)

class Logowanie(models.Model):
    nazwa_uzytkownika = models.CharField(max_length=12, blank=False, unique=True)
    haslo = models.CharField(max_length=12, blank=False, unique=True)

    def __str__(self):
        return self.login_haslo()

    def login_haslo(self):
        return "L: {} H: ({})".format(self.nazwa_uzytkownika, self.haslo)

