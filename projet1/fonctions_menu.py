#affichage du menu principal
def menu_principal():
    print("-------------------------------")
    print("Bienvenue sur le menu principal de votre bibliothèque !")
    print("Que souhaitez-vous faire ?")
    print("1 - Rechercher dans la bibliothèque")
    print("2 - Ajouter un ouvrage à la bibliothèque")
    print("3 - Supprimer un ouvrage de la bibliothèque")
    print("4 - Quitter")
    choix = int(input("Entrez le numéro de l'action choisie : "))
    return choix

#sélection du type de recherche dans la BDD
def menu_recherche():
    print("-------------------------------")
    print("Par quel index souhaitez-vous rechercher ?")
    print("1 - par auteur")
    print("2 - par titre")
    print("3 - par année")
    print("4 - Revenir au menu précédent")
    choix_recherche = int(input("Entrez le numéro de l'action choisie : "))
    return choix_recherche

#fonctionnalités supplémentaires pour la recherche
def fonctionnalites_recherche() :
    print("-------------------------------")
    print("Souhaitez-vous ?")    
    print("1 - Faire une recherche classique (affiche les résultats 5 par 5)")
    print("2 - Afficher plus ou moins de résultats")
    print("3 - Trier les résultats")
    print("4 - Filtrer les résultats")
    print("5 - Revenir au menu précédent")
    choix_fonctionnalite = int(input("Entrez le numéro de l'action choisie : "))
    return choix_fonctionnalite

#limite des résultats 
def limite_resultat() :
    print("-------------------------------")
    choix_limite = int(input("Combien de résultats souhaitez-vous afficher ? "))
    return choix_limite

#fonctionnalités de recherche : trier sur un paramètre    
def param_tri() :  
    print("-------------------------------")
    print("Souhaitez-vous trier ?")  
    print("1 - Trier par auteur")
    print("2 - Trier par titre")
    print("3 - Trier par année")
    print("4 - Revenir au menu précédent")
    choix_param = int(input("Entrez le numéro de l'action choisie : "))
    return choix_param

#fonctionnalités de recherche : trier
def types_tri():
    print("-------------------------------")
    print("Souhaitez-vous trier ?")    
    print("1 - de manière ascendante")
    print("2 - de manière descendante")
    print("3 - Revenir au menu précédent")
    choix_tri = int(input("Entrez le numéro de l'action choisie : "))
    return choix_tri

#fonctionnalités de recherche : filtrer sur un paramètre
def filtre_param() :
    print("-------------------------------")
    print("Souhaitez-vous ?")
    print("1 - Choisir un titre en particulier")
    print("2 - Choisir une année en particulier")
    print("3 - Choisir un auteur en particulier")
    print("4 - Revenir au menu précédent")
    choix_filtre = int(input("Entrez le numéro de l'action choisie : "))
    return choix_filtre 
 
#sélection du type d'ajout à la BDD
def menu_type_ajout():
    print("-------------------------------")
    print("Quel type d'ouvrage souhaitez-vous ajouter ?")
    print("1 - un article")
    print("2 - un livre")
    print("3 - Revenir au menu précédent")
    choix_ajout = int(input("Entrez le numéro de l'action choisie : "))
    return choix_ajout

#sélection du type de suppression 
def menu_choix_suppression() :
    print("-------------------------------")
    print("Que souhaitez-vous supprimer ?")
    print("1 - un seul ouvrage")
    print("2 - plusieurs ouvrages")
    print("3 - Revenir au menu précédent")
    choix_suppression = int(input("Entrez le numéro de l'action choisie : "))
    return choix_suppression

#sélection du type de suppresion multiple 
def menu_supp_multiple():
    print("-------------------------------")
    print("Que souhaitez-vous supprimer ?")
    print("1 - une liste de plusieurs ouvrages")
    print("2 - tous les ouvrages d'un auteur particulier")
    print("3 - tous les ouvrages d'une année particulière")
    print("4 - Revenir au menu précédent")
    choix_supp_multi = int(input("Entrez le numéro de l'action choisie : "))
    return choix_supp_multi

#sélection du nombre d'ouvrages à supprimer
def menu_pls_ouvrages():
    print("-------------------------------")
    nb_ouvrages = int(input("Combien d'ouvrages souhaitez-vous supprimer ? "))
    return nb_ouvrages
    
    
    