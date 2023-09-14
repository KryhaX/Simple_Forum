
from django.contrib import admin
from django.urls import path
from django.urls import include
from konta import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('konta/', include('konta.urls')),
    path('', views.Rejestracja,name='rejestracja'),
    path('logowanie/',views.Logowanie,name='logowanie'),
    path('strona_glowna/',views.StronaGlowna,name='strona_glowna'),
    path('wyloguj/',views.Wyloguj,name='wyloguj')
]
