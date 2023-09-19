from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
# Moje Views
from .models import Pokoj

pokoje = [
    {'id': 1, 'nazwa': 'Test'},
    {'id': 2, 'nazwa': 'Test2'},
    {'id': 3, 'nazwa': 'Test3'}
]


@login_required(login_url='logowanie')
def StronaGlowna(request):
    pokoje = Pokoj.objects.all()

    kontekst = {'pokoje': pokoje}

    return render(request, 'strona_glowna.html', kontekst)


def pokoj(request, pk):
    # Sprawia ze pokazuje sie tytul w pokoj.html
    pokoj = Pokoj.objects.get(id=pk)

    kontekst = {'pokoj': pokoj}

    return render(request, 'pokoj.html', kontekst)


@csrf_protect
def Rejestracja(request):
    if request.method == 'POST':
        nazwa_uzytkownika = request.POST.get('nazwa_uzytkownika')
        email = request.POST.get('email')
        haslo = request.POST.get('haslo')
        powtorz_haslo = request.POST.get('powtorz_haslo')

        if haslo != powtorz_haslo:
            return HttpResponse("Hasła są różne")
        else:
            moj_uzytkownik = User.objects.create_user(nazwa_uzytkownika, email, haslo)
            moj_uzytkownik.save()
            return redirect('logowanie')


    return render(request, 'rejestracja.html')


@csrf_protect
def Logowanie(request):
    if request.method == 'POST':
        nazwa_uzytkownika = request.POST.get('nazwa_uzytkownika')
        haslo = request.POST.get('haslo')
        uzytkownik = authenticate(request, username=nazwa_uzytkownika, password=haslo)

        if uzytkownik is not None:
            login(request, uzytkownik)
            return redirect('strona_glowna')
        else:
            return HttpResponse("Nazwa użytkownika lub hasło nieprawidłowe")

    return render(request, 'logowanie.html')


def Wyloguj(request):
    logout(request)
    return redirect('logowanie')


def stworz_pokoj(request):

    model = Pokoj(request.POST)

    if request.method == "POST":
        tytul = request.POST.get('tytul')
        opis = request.POST.get('opis')
        pokoj = Pokoj.objects.create(tytul=tytul,opis=opis)
        pokoj.save()

        return redirect('strona_glowna')

    return render(request, 'stworz_pokoj.html')
