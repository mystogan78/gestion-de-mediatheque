import os
import django


os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "gestion_de_mediatheque.settings")
django.setup()

from  mediatheque_app.models import Livre, Dvd, Cd, JeuDePlateau, Emprunteur

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Voir les livres")
        print("2. Voir les Dvds")
        print("3. Voir les Cds")
        print("4. Voir les jeu de plateaus")
        print("5. Voir les emprunteurs")
        print("6. Quitter")

        choix = input("Votre choix : ")

        if choix == '1':
            afficher_livres()
        elif choix == '2':
            afficher_dvds()
        elif choix == '3':
            afficher_cds()
        elif choix == '4':
            afficher_jeux()
        elif choix == '5':
            afficher_emprunteurs()
        elif choix == '6':
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


def afficher_livres():
    print("\nListe des livres :")
    for livre in Livre.objects.all():
        print(f"- {livre.name} par {livre.auteur} | Disponible : {'Oui' if livre.disponible else 'Non'}")

def afficher_dvds():
    print("\nListe des DVDs :")
    for dvd in Dvd.objects.all():
        print(f"- {dvd.name} réalisé par {dvd.realisateur} | Disponible : {'Oui' if dvd.disponible else 'Non'}")

def afficher_cds():
    print("\nListe des CDs :")
    for cd in Cd.objects.all():
        print(f"- {cd.name} par {cd.artiste} | Disponible : {'Oui' if cd.disponible else 'Non'}")

def afficher_jeux():
    print("\nListe des jeux de plateau :")
    for jeu in JeuDePlateau.objects.all():
        print(f"- {jeu.name} par {jeu.createur}")

def afficher_emprunteurs():
    print("\nListe des emprunteurs :")
    for emprunteur in Emprunteur.objects.all():
        print(f"- {emprunteur.name} | Bloqué : {'Oui' if emprunteur.bloque else 'Non'}")

if __name__ == '__main__':
    menu()
