from django.db import models
from django.utils import timezone

class Emprunteur(models.Model):
    name = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Classe mère Media
class Media(models.Model):
    name = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Livre(Media):
    auteur = models.CharField(max_length=100)

class Dvd(Media):
    realisateur = models.CharField(max_length=100)

class Cd(Media):
    artiste = models.CharField(max_length=100)

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)


class EmpruntLivre(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)
    date_emprunt = models.DateField(default=timezone.now)
    date_retour = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.livre.name} emprunté par {self.emprunteur.name}"
class EmpruntDvd(models.Model):
    dvd = models.ForeignKey(Dvd, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)  # il manquait ça
    date_emprunt = models.DateField(default=timezone.now)
    date_retour = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.dvd.name} emprunté par {self.emprunteur.name}"


class EmpruntCd(models.Model):
    cd = models.ForeignKey(Cd, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)  # il manquait ça
    date_emprunt = models.DateField(default=timezone.now)
    date_retour = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.cd.name} emprunté par {self.emprunteur.name}"