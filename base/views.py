from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


@login_required(login_url='logowanie')
def StronaGlowna(request):
    return render(request,'strona_glowna.html')


def Rejestracja(request):

    if request.method == 'POST':
        nazwa_uzytkownika = request.POST.get('nazwa_uzytkownika')
        email = request.POST.get('email')
        haslo = request.POST.get('haslo')
        powtorz_haslo = request.POST.get('powtorz_haslo')

        moj_uzytkownik = User.objects.create_user(nazwa_uzytkownika,email,haslo)
        moj_uzytkownik.save()
        return redirect('logowanie')

    # Dodaj ja czeri zrobi powtorz haslo
    # if haslo != powtorz_haslo:
    #     HttpResponse("Hasła są różne")
    # else:
    #     moj_uzytkownik = User.objects.create_user(nazwa_uzytkownika,email,haslo)
    #     moj_uzytkownik.save()
    #     return redirect('logowanie')
    # print(nazwa_uzytkownika,email,haslo)

    return render(request,'rejestracja.html')

@csrf_protect
def Logowanie(request):

    if request.method == 'POST':
        nazwa_uzytkownika = request.POST.get('nazwa_uzytkownika')
        haslo = request.POST.get('haslo')
        uzytkownik = authenticate(request,username=nazwa_uzytkownika,password=haslo)

        if uzytkownik is not None:
            login(request,uzytkownik)
            return redirect('strona_glowna')
        else:
            return HttpResponse("Nazwa użytkownika lub hasło nieprawidłowe")

    return render(request,'logowanie.html')


def Wyloguj(request):
    logout(request)
    return redirect('logowanie')