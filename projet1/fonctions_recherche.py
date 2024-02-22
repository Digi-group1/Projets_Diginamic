import pprint
from fonctions_menu import *

#recherche dans la BDD par auteur
def recherche_auteur(coll, tri=None, type_tri=None, limite=5, filtre=None):
    while True :
        auteur = (input("Entrez les prénom et nom de l'auteur : ")).capitalize()
        if not auteur.isdigit() :
            conditions  = [{"$unwind":"$authors"},{"$match":{"authors":{"$regex":auteur}}}]
            type_tri = "authors"
            pagination_resultats(coll, conditions, tri, type_tri, limite, filtre, f"Voici les ouvrages de l'auteur {auteur} : ")
            break
        else :
            print("Veuillez reformuler votre demande - Le nom de l'auteur ne doit comporter que des lettres")
              
#recherche dans la BDD par année
def recherche_annee(coll,tri=None,type_tri=None,limite=5,filtre=None):
    while True :
        annee_input = input("Entrez l'année de l'ouvrage : ")
        if annee_input.isdigit() == True and len(annee_input) == 4 :
            annee = int(annee_input)
            conditions = [{"$match":{"year":annee}}]
            type_tri = "year"
            pagination_resultats(coll, conditions, tri, type_tri, limite, filtre, f"Voici les ouvrages sortis en {annee} : ")
            break
        else :
            print("Veuillez reformuler votre demande - L'année doit comporter 4 chiffres")

#recherche dans la BDD par titre
def recherche_titre(coll,tri=None,type_tri=None,limite=5,filtre=None) :
    while True :
        titre = input("Entrez le titre de l'ouvrage : ")
        if len(titre) >= 3 :
            conditions = [{"$match":{"title":{"$regex":titre}}}]
            type_tri = "title"
            pagination_resultats(coll, conditions, tri, type_tri, limite, filtre, "Voici l'ouvrage recherché : ")
            break
        else : 
            print("Veuillez reformuler votre demande - Le titre doit comporter au moins 3 caractères")

#fonction pour afficher les résultats sous forme de pagination
def pagination_resultats(coll, conditions_match, tri, type_tri, limite, filtre, message):
    #on établit d'abord si on met des options à la recherche ou non
    choix_option = fonctionnalites_recherche()
    if choix_option == 2 : #On définie une limite particulière
        limite = limite_resultat()
    elif choix_option == 3 : #On veut trier les résultats
        while True : 
            choix_tri = param_tri()
            if choix_tri == 1 : #par auteur
                type_tri = "authors"
            elif choix_tri == 2 : #par titre
                type_tri = "title"
            elif choix_tri == 3 : #par année
                type_tri = "year"
            elif choix_tri == 4 : #revenir au menu précédent
                break
            else : 
                print("Veuillez reformuler votre demande, en insérant un chiffre de 1 à 4")
            facon_tri = types_tri()
            if facon_tri == 1 : #de manière ascendante
                type_tri = 1
                break
            elif facon_tri == 2 : #de manière descendante
                type_tri = -1
                break
            elif facon_tri == 3 : #revenir au menu précédent
                break
            else :
                print("Veuillez reformuler votre demande, en insérant un chiffre entre 1 et 3")
    elif choix_option == 4 : #On veut filtrer les résultats
        while True :
            choix_filtre = filtre_param()
            if choix_filtre == 1 : #on filtre sur un titre en particulier
                titre_filtre = input("Entrez le titre : ")
                filtre = {"title":{"$regex":titre_filtre}}
                break
            elif choix_filtre == 2 : #on filtre sur une année en particulier
                annee_filtre_input = input("Entrez l'année : ")
                annee_filtre = int(annee_filtre_input)
                filtre = {"year":annee_filtre}
                break
            elif choix_filtre == 3 : #on filtre sur un auteur en particulier
                auteur_filtre = input("Entrez le nom de l'auteur : ").capitalize()
                filtre = {"authors":{"$regex":auteur_filtre}}
                break
            elif choix_filtre == 4 : #revenir au menu précédent
                break
                     
    #ensuite on implémente les options
    if conditions_match["authors"] :
        if filtre : 
            conditions = [{"$unwind":"$authors"},{"$match" : {"$and":[conditions_match,filtre]}}]
        else :
            conditions = [{"$unwind":"$authors"},{"$match" : conditions_match}]
    else :
        if filtre:
            conditions = {"$match" : {"$and":[conditions_match,filtre]}}
        else :
            conditions = {"$match" : conditions_match}
        
    if tri:
        conditions.append({"$sort": {tri: type_tri}})
    
    print("-------------------------------")
    print(message)
    
    #calcul du nombre de résultats de la recherche 
    total_results = len(list(coll.aggregate(conditions)))
    if (total_results % limite) == 0 :
        nb_pages = total_results // limite
    else :
        nb_pages = (total_results // limite) + 1
    
    print(f"{total_results} résultats.")
    print("-------------------------------")
    # Ajout des étapes de pagination
    conditions.append({"$skip": 0})
    conditions.append({"$limit": limite})
    page = 1

    while True:
        cursor = coll.aggregate(conditions)
        results = list(cursor)
        total_liste = len(results)
                
        for i in range(total_liste):
            resultat = results[i] 
            resultat_type = resultat['type']
            resultat_titre = resultat['title']
            resultat_year = resultat['year']
            resultat_authors = resultat['authors']
            if resultat_type == "Article" :
                resultat_booktitle = resultat['booktitle']
                print(f"Type : {resultat_type} \nTitre : {resultat_titre} \nAnnée : {resultat_year} \nAuteur(s) : {resultat_authors} \nTitre du livre : {resultat_booktitle}")
                print("-------------------------------")
            if resultat_type == "Book" :
                resultat_publisher = resultat['publisher']
                print(f"Type : {resultat_type} \nTitre : {resultat_titre} \nAnnée : {resultat_year} \nAuteur(s) : {resultat_authors} \nEditeur : {resultat_publisher}")
                print("-------------------------------")
            
            #pprint.pprint(results[i])
            #print(type(results[i]))

        if total_liste < limite:
            print(f"\nPage {page} de {nb_pages} résultats.")
            break
        else:
            print(f"\nPage {page} de {nb_pages} résultats. Appuyez sur 'q' pour quitter, 'p' pour passer à la page suivante.")
            user_input = input()
            if user_input.lower() == 'q':
                break
            elif user_input.lower() == 'p':
                page += 1
                conditions[-2]["$skip"] += limite
                conditions[-1]["$limit"] += limite
            else:
                print("Touche non reconnue. Appuyez sur 'q' pour quitter, 'p' pour passer à la page suivante.")
