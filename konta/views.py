from django.shortcuts import render

# Logowanie i Rejestracja
from .models import Logowanie
from .forms import LogowanieForm # , RejestracjaForm

def logowanie(request):
    # Zmienna przechowująca Form logowania która przyjmuje POST
    form_logowanie = LogowanieForm(request.POST or None)

    if form_logowanie.is_valid():
        logowanie = form_logowanie.save()
        logowanie.save()

    return render(request, 'logowanie.html', {'form_logowanie': form_logowanie})



# Zanim skonczysz widok upewnij się ze rejestracja jest skonczona ( model , urls, forms )

# def rejestracja(request):
#     # Zmienna przechowująca Form rejestracji która przyjmuje POST
#     form_rejestracja = RejestracjaForm(request.POST or None)
#
#     if form_rejestracja.is_valid():
#         rejestracja = form_rejestracja.save()
#         rejestracja.save()
#
#     return render(request, 'logowanie.html', {'form_rejestracja': form_rejestracja})
