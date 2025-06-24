# Projet Django — Gestion de Médiathèque

**Nom :** [Ibrahim KONTE]  
**Date :** [24/06/2025]  

---

## Objectif

Application Web de gestion de médiathèque, développée avec Django.

Elle permet de gérer :

✅ Les livres  
✅ Les DVD  
✅ Les CD  
✅ Les jeux de plateau  

---

## Fonctionnalités

### Application Bibliothécaire

- Créer un emprunteur
- Liste des membres
- Ajouter un média
- Liste des médias
- Créer un emprunt
- Limite de 3 emprunts par membre
- Blocage des membres
- Rendre un emprunt
- Reset complet de la médiathèque

### Application Membre

- Liste des médias consultable

---

## Contraintes respectées

- Les jeux de plateau ne sont pas empruntables
- Un membre ne peut pas avoir + de 3 emprunts
- Les membres bloqués ne peuvent pas emprunter
- Retour des médias géré
- Date de retour enregistrée

---

## Technologies utilisées

- Django 5.x  
- Python 3.x  
- SQLite (base de données par défaut Django)

---

## Installation

1. Cloner le dépôt  
```bash
git clone https://github.com/mystogan78/gestion-de-mediatheque.git
