from django.contrib import admin

# Register your models here.
from .models import Logowanie

# @admin.register(Logowanie)
# class LogowanieAdmin(admin.ModelAdmin):
#     list_display = ["nazwa_uzytkownika", "email", "haslo"]
#     list_filter = ("nazwa_uzytkownika", "email")
#     search_fields = ("nazwa_uzytkownika", "email" )
admin.site.register(Logowanie)


# @admin.register(Rejestracja)
# class RejestracjaAdmin(admin.ModelAdmin):
#     list_display = ["nazwa_uzytkownika", "email", "haslo"]
#     list_filter = ("nazwa_uzytkownika", "email")
#     search_fields = ("nazwa_uzytkownika", "email" )