#import des différents fichiers utiles à l'éxecution du script
from fonctions_menu import *
from fonctions_recherche import *
from fonctions_ajout import *
from fonctions_suppression import *

#import de la BDD MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["my-first-db"]
coll = db['book']
import pprint

#Affichage du menu principal
#Actions réalisées en fonction du choix de l'utilisateur : 
while True : 
    choix = menu_principal()

    if choix == 1 : #On recherche dans la bibliothèque
        while True :
            choix_recherche = menu_recherche()
            if choix_recherche == 1 : #recherche par auteur
                recherche_auteur(coll)              
                break
            elif choix_recherche == 2 : #recherche par titre
                recherche_titre(coll)
                break
            elif choix_recherche == 3 : #recheche par année
                recherche_annee(coll)
                break
            elif choix_recherche == 4 : #revenir au menu précédent
                break                        
     
    elif choix == 2 : #On ajoute à la bibliothèque
        while True :
            choix_ajout = menu_type_ajout()
            if choix_ajout == 1 : #ajoute un article
                ajout_article(coll)
            elif choix_ajout == 2 : #ajoute un livre
                ajout_livre(coll)
            elif choix_ajout == 3 : #revenir au menu précédent
                break

    elif choix == 3 : #On supprime de la bibliothèque
        while True :
            choix_suppression = menu_choix_suppression()
            if choix_suppression == 1 : #suppression unique
                suppression(coll)
            elif choix_suppression == 2 : #suppression multiple
                while True :
                    choix_supp_multi = menu_supp_multiple()
                    if choix_supp_multi == 1 : #liste de plusieurs ouvrages
                        nb_ouvrages = menu_pls_ouvrages()
                    elif choix_supp_multi == 2 : #tous les ouvrages d'un auteur
                        suppression_auteur(coll)
                    elif choix_supp_multi == 3 : #tous les ouvrages d'une année
                        suppression_annee(coll)
                    elif choix_supp_multi == 4 : #revenir au menu précédent
                        break
            elif choix_suppression == 3 : #revenir au menu précédent
                break

    elif choix == 4 : #On quitte
        print("A bientôt !")
        break



