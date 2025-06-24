from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_principal, name='menu_principal'),
    path('menu/', views.menu_principal, name='menu_principal'),
    path('livres/', views.liste_livres, name='liste_livres'),
    path('dvds/', views.liste_dvds, name='liste_dvds'),
    path('cds/', views.liste_cds, name='liste_cds'),
    path('jeux/', views.liste_jeux, name='liste_jeux'),
    path('membres/', views.liste_membres, name='liste_membres'),
    path('creer_emprunt_livre/<int:livre_id>/<int:emprunteur_id>/', views.creer_emprunt_livre,
         name='creer_emprunt_livre'),
    path('creer_emprunt_dvd/<int:dvd_id>/<int:emprunteur_id>/', views.creer_emprunt_dvd, name='creer_emprunt_dvd'),
    path('creer_emprunt_cd/<int:cd_id>/<int:emprunteur_id>/', views.creer_emprunt_cd, name='creer_emprunt_cd'),
    path('rendre_emprunt_livre/<int:emprunt_id>/', views.rendre_emprunt_livre, name='rendre_emprunt_livre'),
    path('rendre_emprunt_dvd/<int:emprunt_id>/', views.rendre_emprunt_dvd, name='rendre_emprunt_dvd'),
    path('rendre_emprunt_cd/<int:emprunt_id>/', views.rendre_emprunt_cd, name='rendre_emprunt_cd'),
    path('reset/', views.reset_medias, name='reset_medias'),



]
