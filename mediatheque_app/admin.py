from django.contrib import admin

from .models import Livre, Dvd, Cd, JeuDePlateau, Emprunteur

@admin.register(Livre)

class LivreAdmin(admin.ModelAdmin):
    list_display =('name', 'auteur', 'disponible' )

@admin.register(Dvd)
class DvdAdmin(admin.ModelAdmin):
    list_display = ('name', 'realisateur', 'disponible' )

@admin.register(Cd)
class CdAdmin(admin.ModelAdmin):
    list_display = ('name', 'artiste', 'disponible')


@admin.register(JeuDePlateau)
class JeuDePlateauAdmin(admin.ModelAdmin):
    list_display = ('name', 'createur')


@admin.register(Emprunteur)
class EmprunteurAdmin(admin.ModelAdmin):
    list_display = ('name', 'bloque')

