#import des fichiers utiles au lancement du programme
from fct_menus import *
from fct_recherches import *
from fct_ajouts import *
from fct_suppressions import *
from fct_statistiques import *

#import de la BDD MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["my-first-db"]
coll = db['books_projet']
import pprint

#appel du menu principal
while True :
    choix_menu_principal = menu_principal()
    
    #on fait des actions en fonction du choix de l'utilisateur
    if choix_menu_principal == 1 : #On recherche dans la bibliothèque 
        #On demande maintenant sur quelle variable l'utilisateur veut rechercher
        while True :
            choix_recherche = menu_recherche()
            if choix_recherche == 1 : #On recherche par auteur
                auteur = rechercher_auteur()
                conditions = [{"$unwind":"$authors"},{"$match":{"authors":{"$regex":auteur}}}]
                message = colorama.Fore.CYAN + " Voici les ouvrages de l'auteur " + colorama.Fore.MAGENTA + f"{auteur}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
            elif choix_recherche == 2 : #On recherche par titre
                titre = rechercher_titre()
                conditions = [{"$match":{"title":{"$regex":titre}}}]
                message = colorama.Fore.CYAN + "Voici les ouvrages portant le titre " + colorama.Fore.MAGENTA + f"{titre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
            elif choix_recherche == 3 : #On recherche par année
                annee = rechercher_annee()
                conditions = [{"$match":{"year":annee}}]
                message = colorama.Fore.CYAN + "Voici les ouvrages sortis en " + colorama.Fore.MAGENTA + f"{annee}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
            elif choix_recherche == 4 : #On recherche par type :
                type = rechercher_type()
                conditions = [{"$match":{"type":type}}]
                if type == "Book" :
                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "livres" + colorama.Fore.CYAN + " présents dans votre bibliothèque : " + colorama.Style.RESET_ALL
                elif type == "Article" :
                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "articles" + colorama.Fore.CYAN + " présents dans votre bibliothèque : " + colorama.Style.RESET_ALL
            elif choix_recherche == 5 : #On revient au menu précédent
                break
            #Puis on demande si l'utilisateur veut des options particulières pour sa recherche :
            while True :
                choix_option = options_recherche()
                limite = 5
                if choix_option == 1 : #On fait une recherche classique
                    pagination_resultats(coll,conditions,None,None,limite,message)
                    break
                elif choix_option == 2 : #On affiche plus ou moins de résultats par page
                    limite = limite_affichage()
                    pagination_resultats(coll,conditions,None,None,limite,message)
                    break
                elif choix_option == 3 : #On trie les résultats
                    while True :
                        choix_tri = options_tri()
                        if choix_tri == 1 : #On trie par auteur
                            tri = "authors"
                        elif choix_tri == 2 : #On trie par titre
                            tri = "title"
                        elif choix_tri == 3 : #On trie par année
                            tri = "year"
                        elif choix_tri == 4 : #On revient au menu précédent
                            break
                        while True :
                            choix_sens = sens_tri()
                            if choix_sens == 1 : #On trie de manière ascendante
                                type_tri = 1
                                pagination_resultats(coll,conditions,tri,type_tri,limite,message)
                                break
                            elif choix_sens == 2 : #On trie de manière descendante
                                type_tri = -1
                                pagination_resultats(coll,conditions,tri,type_tri,limite,message)
                                break
                            elif choix_sens == 3 : #On revient au menu précédent
                                break   
                        break
                elif choix_option == 4 : #On filtre les résultats
                    while True :
                        choix_filtre = selection_filtre()
                        limite = 5
                        if choix_filtre == 1 : #on veut filtrer par titre
                            titre_filtre = rechercher_titre()  
                            if choix_recherche == 1 : #on a une liste pour un auteur
                                conditions = [{"$unwind":"$authors"},{"$match":{"$and":[{"authors":{"$regex":auteur}},{"title":{"$regex":titre_filtre}}]}}]
                                message = colorama.Fore.CYAN + "Voici les ouvrages de l'auteur " + colorama.Fore.MAGENTA + f"{auteur}" + colorama.Fore.CYAN + " dont le titre est "  + colorama.Fore.MAGENTA + f"{titre_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 2 : #On a une liste pour un titre
                                conditions = [{"$match":{"$and":[{"title":{"$regex":titre}},{"title":{"$regex":titre_filtre}}]}}]
                                message = colorama.Fore.CYAN + "Voici les ouvrages portant les titres " + colorama.Fore.MAGENTA + f"{titre}" + colorama.Fore.CYAN + " et "  + colorama.Fore.MAGENTA + f"{titre_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 3 : #On a une liste pour une année
                                conditions = [{"$match":{"$and":[{"year":annee},{"title":{"$regex":titre_filtre}}]}}]
                                message = colorama.Fore.CYAN + "Voici les ouvrages sortis en " + colorama.Fore.MAGENTA + f"{annee}" + colorama.Fore.CYAN + " dont le titre est "  + colorama.Fore.MAGENTA + f"{titre_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 4 : #On a une liste pour un type d'ouvrage
                                conditions = [{"$match":{"$and":[{"type":type},{"title":{"$regex":titre_filtre}}]}}]
                                if type == "Book" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "livres" + colorama.Fore.CYAN + " dont le titre est "  + colorama.Fore.MAGENTA + f"{titre_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                                elif type == "Article" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "articles" + colorama.Fore.CYAN + " dont le titre est "  + colorama.Fore.MAGENTA + f"{titre_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                        elif choix_filtre == 2 : #on veut filtrer par année
                            annee_filtre = rechercher_annee()
                            if choix_recherche == 1 : #on a une liste pour un auteur
                                conditions = [{"$unwind":"$authors"},{"$match":{"$and":[{"authors":{"$regex":auteur}},{"year":annee_filtre}]}}]
                                message = colorama.Fore.CYAN + "Voici les ouvrages de l'auteur " + colorama.Fore.MAGENTA + f"{auteur}" + colorama.Fore.CYAN + " sortis en "  + colorama.Fore.MAGENTA + f"{annee_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 2 : #on a une liste pour un titre
                                conditions = [{"$match":{"$and":[{"title":{"$regex":titre}},{"year":annee_filtre}]}}]
                                message = colorama.Fore.CYAN + "Voici les ouvrages portant le titre " + colorama.Fore.MAGENTA + f"{titre}" + colorama.Fore.CYAN + " sortis en "  + colorama.Fore.MAGENTA + f"{annee_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 3 : #On a une liste pour une année
                                conditions = [{"$match":{"$or":[{"year":annee},{"year":annee_filtre}]}}]
                                message = colorama.Fore.CYAN + "Voici les ouvrages sortis en " + colorama.Fore.MAGENTA + f"{annee}" + colorama.Fore.CYAN + " ou en "  + colorama.Fore.MAGENTA + f"{annee_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 4 : #On a une liste pour un type d'ouvrage
                                conditions = [{"$match":{"$and":[{"type":type},{"year":annee_filtre}]}}]
                                if type == "Book" :
                                    message = colorama.Fore.CYAN + "Voici les ouvrages " + colorama.Fore.MAGENTA + "livres" + colorama.Fore.CYAN + " sortis en "  + colorama.Fore.MAGENTA + f"{annee_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                                elif type == "Article" :
                                    message = colorama.Fore.CYAN + "Voici les ouvrages " + colorama.Fore.MAGENTA + "articles" + colorama.Fore.CYAN + " sortis en "  + colorama.Fore.MAGENTA + f"{annee_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                        elif choix_filtre == 3 : #On veut filtrer par auteur
                            auteur_filtre = rechercher_auteur()
                            if choix_recherche == 1 : #on a une liste pour un auteur
                                conditions = [{"$unwind":"$authors"},{"$match":{"$and":[{"authors":{"$regex":auteur}},{"authors":{"$regex":auteur_filtre}}]}}]
                                message = colorama.Fore.CYAN + "Voici les ouvrages des auteurs " + colorama.Fore.MAGENTA + f"{auteur}" + colorama.Fore.CYAN + " et "  + colorama.Fore.MAGENTA + f"{auteur_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 2 : #on a une liste pour un titre
                                conditions = [{"$unwind":"$authors"},{"$match":{"$and":[{"title":{"$regex":titre}},{"authors":{"$regex":auteur_filtre}}]}}]
                                message = colorama.Fore.CYAN + "Voici les ouvrages portant le titre " + colorama.Fore.MAGENTA + f"{titre}" + colorama.Fore.CYAN + " de l'auteur "  + colorama.Fore.MAGENTA + f"{auteur_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 3 : #On a une liste pour une année
                                conditions = [{"$unwind":"$authors"},{"$match":{"$and":[{"year":annee},{"authors":{"$regex":auteur_filtre}}]}}]
                                message = colorama.Fore.CYAN + "Voici les ouvrages sortis en " + colorama.Fore.MAGENTA + f"{annee}" + colorama.Fore.CYAN + " de l'auteur "  + colorama.Fore.MAGENTA + f"{auteur_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 4 : #On a une liste pour un type d'ouvrage
                                conditions = [{"$unwind":"$authors"},{"$match":{"$and":[{"type":type},{"authors":{"$regex":auteur_filtre}}]}}]
                                if type == "Book" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "livres" + colorama.Fore.CYAN + " de l'auteur "  + colorama.Fore.MAGENTA + f"{auteur_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                                elif type == "Article" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "articles" + colorama.Fore.CYAN + " de l'auteur "  + colorama.Fore.MAGENTA + f"{auteur_filtre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                        elif choix_filtre == 4 : #On veut filtrer par type
                            type_filtre = rechercher_type()
                            if choix_recherche == 1 : #on a une liste pour un auteur
                                conditions = [{"$unwind":"$authors"},{"$match":{"$and":[{"authors":{"$regex":auteur}},{"type":type_filtre}]}}]
                                if type_filtre == "Book" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "livres" + colorama.Fore.CYAN + " de l'auteur "  + colorama.Fore.MAGENTA + f"{auteur}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                                elif type_filtre == "Article" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "articles" + colorama.Fore.CYAN + " de l'auteur "  + colorama.Fore.MAGENTA + f"{auteur}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 2 : #on a une liste pour un titre
                                conditions = [{"$match":{"$and":[{"title":{"$regex":titre}},{"type":type_filtre}]}}]
                                if type_filtre == "Book" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "livres" + colorama.Fore.CYAN + " portant le titre "  + colorama.Fore.MAGENTA + f"{titre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                                elif type_filtre == "Article" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "articles" + colorama.Fore.CYAN + " portant le titre "  + colorama.Fore.MAGENTA + f"{titre}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 3 : #On a une liste pour une année
                                conditions = [{"$match":{"$and":[{"year":annee},{"type":type_filtre}]}}]
                                if type_filtre == "Book" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "livres" + colorama.Fore.CYAN + " sortis en "  + colorama.Fore.MAGENTA + f"{annee}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                                elif type_filtre == "Article" :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "articles" + colorama.Fore.CYAN + " sortis en "  + colorama.Fore.MAGENTA + f"{annee}" + colorama.Fore.CYAN + " : " + colorama.Style.RESET_ALL
                            elif choix_recherche == 4 : #On a une liste pour un type d'ouvrage
                                conditions = [{"$match":{"$or":[{"type":type},{"type":type_filtre}]}}]
                                if type != type_filtre :
                                    message = colorama.Fore.CYAN + "Voici les " + colorama.Fore.MAGENTA + "livres" + colorama.Fore.CYAN + " et "  + colorama.Fore.MAGENTA + "articles" + colorama.Fore.CYAN + " présents dans votre bibliothèque : " + colorama.Style.RESET_ALL

                        elif choix_filtre == 5 : #On revient au menu précédent
                            break
                        pagination_resultats(coll,conditions,None,None,limite,message)
                        break
                elif choix_option == 5 : #On revient au menu précédent
                    break
    elif choix_menu_principal == 2 : #On ajoute un ouvrage à la bibliothèque
        while True :
            choix_ajout = ajout_ouvrage()
            if choix_ajout == 1 : #On ajoute un article
                ajout_article(coll)
                break
            elif choix_ajout == 2 : #On ajout un livre
                ajout_livre(coll)
                break
            elif choix_ajout == 3 : #On ajout un phd
                ajout_phd(coll)
                break
            elif choix_ajout == 4 : #On revient au menu précédent
                break
    elif choix_menu_principal == 3 : #On supprime un ouvrage à la bibliothèque
        while True :
            choix_suppression = suppression_ouvrage()
            if choix_suppression == 1 : #On supprime un ouvrage
                suppression(coll)
                break
            elif choix_suppression == 2 : #On supprime plusieurs ouvrages
                while True :
                    choix_multi = suppressions_multi()
                    if choix_multi == 1 : #liste de plusieurs ouvrages
                        nb_ouvrages = pls_ouvrages()
                        suppression_multiple(coll,nb_ouvrages)
                        break
                    elif choix_multi == 2 : #tous les ouvrages d'un auteur
                        suppression_auteur(coll)
                        break
                    elif choix_multi == 3 : #tous les ouvrages d'une année
                        suppression_annee(coll)
                        break
                    elif choix_multi == 4 : #tous les ouvrages d'un type
                        suppression_type(coll)
                        break
                    elif choix_multi == 5 : #On revient au menu précédent
                        break
            elif choix_suppression == 3 : #On revient au menu précédent
                break
    elif choix_menu_principal == 4 : #On affiche les statistiques
        while True :
            choix_stats = options_stats()
            if choix_stats == 1 : #statistiques basiques
                print(colorama.Fore.CYAN + "-------------------------------" + colorama.Style.RESET_ALL)
                nb_publi(coll)
                moyenne_annee(coll)
                moyenne_auteur(coll) 
            elif choix_stats == 2 : #statistiques détaillées
                while True :
                    choix_detaille = stats_detaillees_choix()
                    if choix_detaille == 1 : #le nb de publications par année
                        print(colorama.Fore.CYAN + "-------------------------------" + colorama.Style.RESET_ALL)
                        nb_publi_annee_agg(coll)
                    elif choix_detaille == 2 : #le nb de publications par type
                        print(colorama.Fore.CYAN + "-------------------------------" + colorama.Style.RESET_ALL)
                        nb_publi_type_agg(coll)
                    elif choix_detaille == 3 : #le top des auteurs prolifiques
                        nb_affiche = limite_top()
                        print(colorama.Fore.CYAN + "-------------------------------" + colorama.Style.RESET_ALL)
                        auteurs_prolifiques(coll,nb_affiche)
                    elif choix_detaille == 4 : #le top des années prolifiques
                        nb_affiche = limite_top()
                        print(colorama.Fore.CYAN + "-------------------------------" + colorama.Style.RESET_ALL)
                        annees_prolifiques(coll,nb_affiche)
                    elif choix_detaille == 5 : #le nb de publications par auteur
                        print(colorama.Fore.CYAN + "-------------------------------" + colorama.Style.RESET_ALL)
                        nb_publi_auteur_agg(coll)
                    elif choix_detaille == 6 : #On revient au menu précédent
                        break
            elif choix_stats == 3 : #Revenir au menu précédent
                print(colorama.Fore.YELLOW + "~~~~ Merci de votre attention ~~~~" + colorama.Style.RESET_ALL)
                break
    elif choix_menu_principal == 5 : #On quitte
        print(colorama.Fore.RED + "A" + " " + colorama.Fore.YELLOW + "b" + colorama.Fore.GREEN + "i" + colorama.Fore.BLUE + "e" + colorama.Fore.MAGENTA + "n" + colorama.Fore.BLUE + "t" + colorama.Fore.GREEN + "ô" + colorama.Fore.YELLOW + "t" + " " + colorama.Fore.RED + "!" + colorama.Style.RESET_ALL)
        break

    
    