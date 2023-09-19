
from django.contrib import admin
from django.urls import path
from django.urls import include
from base import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include('base.urls')),
    path('', views.Rejestracja,name='rejestracja'),
    path('logowanie/',views.Logowanie,name='logowanie'),
    path('strona_glowna/',views.StronaGlowna,name='strona_glowna'),
    path('wyloguj/',views.Wyloguj,name='wyloguj'),
    path('pokoj/<str:pk>',views.pokoj,name='pokoj'),
    path('stworz_pokoj',views.stworz_pokoj,name='stworz_pokoj'),

]
