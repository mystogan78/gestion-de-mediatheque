from django.test import TestCase
from .models import Emprunteur, Livre, EmpruntLivre
from django.utils import timezone

class EmpruntLivreTest(TestCase):
    def setUp(self):
        self.emprunteur = Emprunteur.objects.create(name="Test Membre", bloque=False)
        self.livre = Livre.objects.create(name="Test Livre", auteur="Auteur Test", disponible=True)

    def test_creer_emprunt_livre(self):
        # Créer un emprunt
        emprunt = EmpruntLivre.objects.create(
            livre=self.livre,
            emprunteur=self.emprunteur,
            date_emprunt=timezone.now(),
            date_retour=None
        )
        # Vérifier que l'emprunt existe
        self.assertEqual(EmpruntLivre.objects.count(), 1)
        self.assertEqual(emprunt.livre, self.livre)
        self.assertEqual(emprunt.emprunteur, self.emprunteur)


# Create your tests here.
