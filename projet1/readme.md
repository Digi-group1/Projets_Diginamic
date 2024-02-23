<h1 align="center">Projet Système de gestion d'une bibliothèque</h1>

## :point_down: Groupe 1 Diginamic :
3 membres : Amandine André, Andréa Le Marec et Anthony Alves

## :point_down: Objectifs :

L'objectif de ce projet est de créer un système de gestion de bibliothèque en ligne de commande: <br>
👉 Depuis une base de données "Books" au format json (qui n'est pas présente dans le github car trop lourde) <br>
👉 Avec 4 fonctionnalités proposées à l'utilisateur : <br>
- Recherche dans la bibliothèque <br>
- Ajout d'un ouvrage <br>
- Suppression d'un ouvrage <br>
- Affichage de statistiques de la bibliothèques <br>

## :point_down: Prérequis :
Notre système de gestion utilise :
###### Languages
- Python (version 3.11)
###### Librairies additionnelles
- Affichage : pprint
- Coloration : colorama
- Fonctions mathématiques : math
- Interactions MongoDB/Python : pymongo​
- Sérialisation : bson.objectid

## 🚀&nbsp; Présentation des différents fichiers
#### main.py
👉 Fichier principal, qui est à lancer pour afficher le système de gestion en ligne de commande <br>
```
py main.py
```
#### fct_ajouts.py
👉 Liste toutes les fonctions utiles pour ajouter un ou plusieurs ouvrages dans la bibliothèque
#### fct_menus.py
👉 Liste toutes les fonctions utiles pour l'affichage des différents menus
#### fct_recherches.py
👉 Liste toutes les fonctions utiles pour rechercher un ou plusieurs ouvrages dans la bibliothèque 
#### fct_statistiques.py
👉 Liste toutes les fonctions utiles pour afficher les statistiques descriptives de la bibliothèque
#### fct_suppressions.py
👉 Liste toutes les fonctions utiles pour supprimer un ou plusieurs ouvrages dans la bibliothèque
