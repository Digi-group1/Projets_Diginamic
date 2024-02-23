import colorama
import math

#On fait une fonction pour afficher le nombre de publications :
def nb_publi(coll) :
    count = coll.count_documents({})
    print(colorama.Fore.CYAN + "Nombre de publications totales : " + colorama.Fore.MAGENTA + f"{count}" + colorama.Style.RESET_ALL)

#On fait une fonction pour afficher le nombre de publications par année
def nb_publi_annee_agg(coll) :
    cursor = coll.aggregate([{"$group":{"_id":"$year","nb":{"$sum":1}}},{"$sort":{"_id":1}}])
    results = list(cursor)
    total_liste = len(results)
                
    for i in range(total_liste):
        resultat = results[i] 
        resultat_annee = resultat['_id']
        resultat_nb = resultat['nb']
        print(colorama.Fore.CYAN + "Année : " + colorama.Fore.YELLOW + f"{resultat_annee}" + colorama.Fore.CYAN + ", Nombres de publications : " + colorama.Fore.YELLOW + f"{resultat_nb}" + colorama.Style.RESET_ALL)

#On fait une fonction pour afficher le nombre de publications par type
def nb_publi_type_agg(coll) :
    cursor = coll.aggregate([{"$group":{"_id":"$type","nb":{"$sum":1}}},{"$sort":{"_id":1}}])
    results = list(cursor)
    total_liste = len(results)
                
    for i in range(total_liste):
        resultat = results[i] 
        resultat_type = resultat['_id']
        resultat_nb = resultat['nb']
        print(colorama.Fore.CYAN + "Type : " + colorama.Fore.YELLOW + f"{resultat_type}" + colorama.Fore.CYAN + ", Nombres de publications : " + colorama.Fore.YELLOW + f"{resultat_nb}" + colorama.Style.RESET_ALL)

#On fait une fonction pour afficher le nombre de publications par auteur
def nb_publi_auteur_agg(coll) :
    cursor = coll.aggregate([{"$unwind":"$authors"},{"$group":{"_id":"$authors","nb":{"$sum":1}}},{"$sort":{"_id":1}}])
    results = list(cursor)
    total_liste = len(results)
                
    for i in range(total_liste):
        resultat = results[i] 
        resultat_auteur = resultat['_id']
        resultat_nb = resultat['nb']
        print(colorama.Fore.CYAN + "Auteur : " + colorama.Fore.YELLOW + f"{resultat_auteur}" + colorama.Fore.CYAN + ", Nombres de publications : " + colorama.Fore.YELLOW + f"{resultat_nb}" + colorama.Style.RESET_ALL)

#On fait une fonction pour afficher les auteurs les plus prolifiques :
def auteurs_prolifiques(coll,nb_affiche) :
    cursor = coll.aggregate([{"$unwind":"$authors"},{"$group":{"_id":"$authors","nb":{"$sum":1}}},{"$sort":{"nb":-1}},{"$limit":nb_affiche}])
    results = list(cursor)
    total_liste = len(results)
                
    for i in range(total_liste):
        resultat = results[i] 
        resultat_auteur = resultat['_id']
        resultat_nb = resultat['nb']
        print(colorama.Fore.CYAN + "Auteur : " + colorama.Fore.YELLOW + f"{resultat_auteur}" + colorama.Fore.CYAN + ", Nombres de publications : " + colorama.Fore.YELLOW + f"{resultat_nb}" + colorama.Style.RESET_ALL)

#On fait une fonction pour afficher les années les plus prolifiques :  
def annees_prolifiques(coll,nb_affiche) :
    cursor = coll.aggregate([{"$group":{"_id":"$year","nb":{"$sum":1}}},{"$sort":{"_id":1}},{"$sort":{"nb":-1}},{"$limit":nb_affiche}])
    results = list(cursor)
    total_liste = len(results)
                
    for i in range(total_liste):
        resultat = results[i] 
        resultat_annee = resultat['_id']
        resultat_nb = resultat['nb']
        print(colorama.Fore.CYAN + "Année : " + colorama.Fore.YELLOW + f"{resultat_annee}" + colorama.Fore.CYAN + ", Nombres de publications : " + colorama.Fore.YELLOW + f"{resultat_nb}" + colorama.Style.RESET_ALL)
  

#On fait une fonction pour afficher la moyenne de publications par année
def moyenne_annee(coll) :
    #On liste les années
    distinct_annee = coll.distinct("year")
    nb_annee = len(distinct_annee)
    #On fait un dico pour stocker le nb d'enregistrements par année
    count = coll.count_documents({})
    #On fait la moyenne
    moyenne = int(math.ceil(count / nb_annee))
    print(colorama.Fore.CYAN + "Nombre de publications moyennes par an : " + colorama.Fore.MAGENTA + f"{moyenne}" + colorama.Style.RESET_ALL)

#On fait une fonction pour afficher la moyenne de publications par auteur
def moyenne_auteur(coll) :
    #On liste les années
    distinct_auteur = coll.distinct("authors")
    nb_auteur = len(distinct_auteur)
    #On fait un dico pour stocker le nb d'enregistrements par année
    count = coll.count_documents({})
    #On fait la moyenne
    moyenne = int(math.ceil(count / nb_auteur))
    print(colorama.Fore.CYAN + "Nombre de publications moyennes par auteur : " + colorama.Fore.MAGENTA + f"{moyenne}" + colorama.Style.RESET_ALL)


#On fait une fonction pour déterminer le nombre d'affichages par page
def limite_top() :
    while True :
        limite_input = input(colorama.Fore.YELLOW + "Combien de résultats souhaitez-vous afficher : " + colorama.Style.RESET_ALL)
        if limite_input.isdigit() :
            limite = int(limite_input)
            break
        else :
            print(colorama.Fore.RED + "Veuillez reformuler votre demande - en inscrivant un nombre " + colorama.Style.RESET_ALL)
    return limite    


