from django.shortcuts import render
from django.http import HttpResponse
from .models import Livre, Dvd, Cd, JeuDePlateau, Emprunteur, EmpruntLivre, EmpruntDvd, EmpruntCd
from django.utils import timezone


def menu_principal(request):
    return render(request, 'menu.html')

def liste_livres(request):
    livres = Livre.objects.all()
    emprunts_actifs = EmpruntLivre.objects.filter(date_retour__isnull=True)

    # DEBUG :
    print("DEBUG - Emprunts actifs :")
    for e in emprunts_actifs:
        print(f"ID emprunt: {e.id}, Livre: {e.livre.name}, Emprunteur: {e.emprunteur.name}, Date retour: {e.date_retour}")

    for livre in livres:
        emprunt = EmpruntLivre.objects.filter(livre=livre, date_retour__isnull=True).first()
        livre.emprunt_en_cours = emprunt

    return render(request, 'livres.html', {
        'livres': livres,
        'emprunts_actifs': emprunts_actifs
    })




def liste_dvds(request):
    dvds = Dvd.objects.all()
    emprunts_actifs = EmpruntDvd.objects.filter(date_retour__isnull=True)

    #DEBUG
    print("DEBUG - Emprunts actifs :")
    for e in emprunts_actifs:
        print(f"ID emprunt:{e.id}, Dvd: {e.dvd.name}, Date retour: {e.date_retour}")

    for dvd in dvds:
        emprunt = EmpruntDvd.objects.filter(dvd=dvd, date_retour__isnull=True).first()
        dvd.emprunt_en_cours = emprunt


    return render(request, 'dvds.html', {'dvds': dvds,'emprunts_actifs': emprunts_actifs})

def liste_cds(request):
    cds = Cd.objects.all()
    emprunts_actifs = EmpruntCd.objects.filter(date_retour__isnull=True)


    #DEBUG
    print("DEBUG - Emprunts actifs :")
    for e in emprunts_actifs:
        print(f"ID emprunt:{e.id}, Cd: {e.cd.name}, Date retour: {e.date_retour}")

    for cd in cds:
        emprunt = EmpruntCd.objects.filter(cd=cd, date_retour__isnull=True).first()
        cd.emprunt_en_cours = emprunt
    return render(request, 'cds.html', {'cds': cds, 'emprunts_actifs': emprunts_actifs})

def liste_jeux(request):
    jeux = JeuDePlateau.objects.all()
    return render(request, 'jeux.html', {'jeux': jeux})

def liste_membres(request):
    membres = Emprunteur.objects.all()   # correction ici
    return render(request, 'membres.html', {'membres': membres})
# === Fonction Emprunt objet ===
def creer_emprunt_livre(request, livre_id, emprunteur_id):
    membre = Emprunteur.objects.get(id=emprunteur_id)

    # vérifier s'il est bloqué
    if membre.bloque:
        return HttpResponse("Ce membre est bloqué et ne peut pas emprunter.")

    # vérifier les emprunts en cours
    emprunts_en_cours = EmpruntLivre.objects.filter(emprunteur=membre, date_retour__isnull=True).count()
    if emprunts_en_cours >= 3:
        return HttpResponse("Ce membre a déjà 3 emprunts en cours !")

    # vérifier si le livre est disponible
    livre = Livre.objects.get(id=livre_id)
    if not livre.disponible:
        return HttpResponse("Ce livre est déjà emprunté.")

    # Créer l'emprunt → PAS de date_retour à la création
    EmpruntLivre.objects.create(
        livre=livre,
        emprunteur=membre,
        date_emprunt=timezone.now(),
        date_retour=None  # C'est la clé ! On ne met pas encore la date de retour
    )

    # mettre à jour le livre
    livre.disponible = False
    livre.save()

    return HttpResponse(f"Le livre '{livre.name}' a bien été emprunté par {membre.name} !")

def creer_emprunt_dvd(request, dvd_id, emprunteur_id):
    membre = Emprunteur.objects.get(id=emprunteur_id)

    #Verifier si il est bloqué

    if membre.bloque:
        return HttpResponse("Ce membre est bloqué et ne peut pas emprunter.")

    emprunts_en_cours = EmpruntDvd.objects.filter(emprunteur=membre, date_retour__isnull=True).count()
    if emprunts_en_cours >= 3:
        return HttpResponse("Ce membre a déjà 3 emprunts en cours !")

   #Vérifier si le livre est disponible
    dvd: Dvd = Dvd.objects.get(id=dvd_id)
    if not dvd.disponible:
        return HttpResponse("Ce dvd est déja emprunté.")

    #Créer l'emprunt -> pas de retour à la création

    EmpruntDvd.objects.create(
        dvd=dvd,
        emprunteur=membre,
        date_emprunt=timezone.now(),
        date_retour=None
    )
    #mettre à jour le Dvd
    dvd.disponible = False
    dvd.save()

    return HttpResponse(f"Le DVD '{dvd.name}' a bien été emprunté par {membre.name} !")
def creer_emprunt_cd(request, cd_id, emprunteur_id):
    membre = Emprunteur.objects.get(id=emprunteur_id)

    #Vérifier si le membre est bloqué
    if membre.bloque:
        return HttpResponse("Ce membre est bloqué et ne peut pas emprunter.")

    emprunts_en_cours = EmpruntCd.objects.filter(emprunteur=membre, date_retour__isnull=True).count()



    if emprunts_en_cours >= 3:
        return HttpResponse("Ce membre a déjà 3 emprunts en cours !")

    #Vérifier si le cd est disponible

    cd = Cd.objects.get(id=cd_id)
    if not cd.disponible:
        return HttpResponse("Ce cd est déja emprunté.")


    EmpruntCd.objects.create(
        cd=cd,
        emprunteur=membre,
        date_emprunt=timezone.now(),
        date_retour=None
    )


    #mettre à jour le cd


    cd.disponible = False
    cd.save()

    return HttpResponse(f"Le CD '{cd.name}' a bien été emprunté par {membre.name} !")


# === Fonctions rendre emprunt ===

def rendre_emprunt_livre(request, emprunt_id):
    emprunt = EmpruntLivre.objects.get(id=emprunt_id)

    if emprunt.date_retour is not None:
        return HttpResponse("Ce livre a déjà été rendu.")

    # Marquer le livre comme rendu aujourd’hui
    emprunt.date_retour = timezone.now()
    emprunt.save()

    # Remettre le livre disponible
    emprunt.livre.disponible = True
    emprunt.livre.save()

    return HttpResponse(f"Le livre '{emprunt.livre.name}' a bien été rendu par {emprunt.emprunteur.name}.")

def rendre_emprunt_dvd(request, emprunt_id):
    emprunt = EmpruntDvd.objects.get(id=emprunt_id)
    emprunt.date_retour = timezone.now()
    emprunt.save()

    emprunt.dvd.disponible = True
    emprunt.dvd.save()

    return HttpResponse(f"DVD '{emprunt.dvd.name}' rendu par {emprunt.emprunteur.name}.")

def rendre_emprunt_cd(request, emprunt_id):
    emprunt = EmpruntCd.objects.get(id=emprunt_id)
    emprunt.date_retour = timezone.now()
    emprunt.save()

    emprunt.cd.disponible = True
    emprunt.cd.save()

    return HttpResponse(f"CD '{emprunt.cd.name}' rendu par {emprunt.emprunteur.name}.")

def reset_medias(request):
    # Remet tous les livres en disponible
    Livre.objects.update(disponible=True)
    # Supprime les emprunts en cours
    EmpruntLivre.objects.all().delete()

    # Remet tous les dvds en disponible
    Dvd.objects.update(disponible=True)
    # Supprime les emprunts en cours
    EmpruntDvd.objects.all().delete()

    # Remet tous les cds en disponible
    Cd.objects.update(disponible=True)
    # Supprime les emprunts en cours
    EmpruntCd.objects.all().delete()



    return HttpResponse("Médiathèque réinitialisée !")
