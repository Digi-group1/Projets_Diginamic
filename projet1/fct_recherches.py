import pprint
import colorama

#On fait une fonction pour rechercher par auteur
def rechercher_auteur() :
    while True :
        auteur_input = input(colorama.Fore.YELLOW + "Entrez le nom de l'auteur : " + colorama.Style.RESET_ALL).title()
        if not auteur_input.isdigit() :
            auteur = auteur_input
            break
        else :
            print(colorama.Fore.RED + "Veuillez reformuler votre demande - Le nom de l'auteur ne doit pas comporter de caractères spéciaux, que des lettres" + colorama.Style.RESET_ALL)
    return auteur

#On fait une fonction pour rechercher par titre
def rechercher_titre() :
    while True :
        titre_input = input(colorama.Fore.YELLOW + "Entrez le titre de l'ouvrage : " + colorama.Style.RESET_ALL).capitalize()
        if len(titre_input) >= 3 :
            titre = titre_input
            break
        else :
            print(colorama.Fore.RED + "Veuillez reformuler votre demande - Le titre de l'ouvrage doit comporter au moins 3 caractères" + colorama.Style.RESET_ALL)
    return titre

#On fait une fonction pour rechercher par année
def rechercher_annee() :
    while True :
        annee_input = input(colorama.Fore.YELLOW + "Entrez l'année de parution de l'ouvrage : " + colorama.Style.RESET_ALL)
        if annee_input.isdigit() and len(annee_input) == 4 :
            annee = int(annee_input)
            break
        else :
            print(colorama.Fore.RED + "Veuillez reformuler votre demande - L'année doit comporter 4 chiffres" + colorama.Style.RESET_ALL)
    return annee

#On fait une fonction pour rechercher par type
def rechercher_type() :
    while True :
        type_input = input(colorama.Fore.YELLOW + "Entrez le type recherché (livre, article ou phd) : " + colorama.Style.RESET_ALL)
        if type_input.lower() == "livre" :
            type = "Book"
            break
        elif type_input.lower() == "article" :
            type = "Article"
            break
        elif type_input.lower() == "phd" :
            type = "Phd"
            break
        else :
            print(colorama.Fore.RED + "Veuillez reformuler votre demande - en inscrivant livre, article ou phd" + colorama.Style.RESET_ALL)
    return type 

#On fait une fonction pour déterminer le nombre d'affichages par page
def limite_affichage() :
    while True :
        limite_input = input(colorama.Fore.YELLOW + "Combien de résultats souhaitez-vous afficher par page : " + colorama.Style.RESET_ALL)
        if limite_input.isdigit() :
            limite = int(limite_input)
            break
        else :
            print(colorama.Fore.RED + "Veuillez reformuler votre demande - en inscrivant un nombre " + colorama.Style.RESET_ALL)
    return limite

#On fait une fonction pour afficher les résultats sous forme de pagination
def pagination_resultats(coll, conditions, tri, type_tri, limite, message):
    
    if tri:
        conditions.append({"$sort": {tri: type_tri}})
    
    print(colorama.Fore.YELLOW + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + message + colorama.Style.RESET_ALL)
    
    #calcul du nombre de résultats de la recherche 
    total_results = len(list(coll.aggregate(conditions)))
    if (total_results % limite) == 0 :
        nb_pages = total_results // limite
    else :
        nb_pages = (total_results // limite) + 1
    
    print(colorama.Fore.MAGENTA + f"{total_results}" + colorama.Fore.YELLOW + " résultats." + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "-------------------------------" + colorama.Style.RESET_ALL)
    # Ajout des étapes de pagination
    conditions.append({"$skip": 0})
    conditions.append({"$limit": limite})
    page = 1

    while True:
        cursor = coll.aggregate(conditions)
        results = list(cursor)
        total_liste = len(list(coll.aggregate(conditions)))
                
        for i in range(total_liste):
            resultat = results[i] 
            resultat_id = resultat['_id']
            resultat_type = resultat['type']
            resultat_titre = resultat['title']
            resultat_year = resultat['year']
            resultat_authors = resultat['authors']
            print(colorama.Fore.CYAN + f"Id : {resultat_id} \nType : {resultat_type} \nTitre : {resultat_titre} \nAnnée : {resultat_year} \nAuteur(s) : {resultat_authors}")
            print("-------------------------------" + colorama.Style.RESET_ALL)
            
            #pprint.pprint(results[i])
            #print(type(results[i]))

        if total_liste < limite:
            print(colorama.Fore.YELLOW + f"\nPage {page} de {nb_pages} pages." + colorama.Style.RESET_ALL)
            break
        else:
            print(colorama.Fore.YELLOW + f"\nPage {page} de {nb_pages} pages. Appuyez sur 'q' pour quitter, 'p' pour passer à la page suivante." + colorama.Style.RESET_ALL)
            user_input = input()
            if user_input.lower() == 'q':
                break
            elif user_input.lower() == 'p':
                page += 1
                conditions[-2]["$skip"] += limite
                conditions[-1]["$limit"] += limite
            else:
                print(colorama.Fore.RED + "Touche non reconnue. Appuyez sur 'q' pour quitter, 'p' pour passer à la page suivante." + colorama.Style.RESET_ALL)


       