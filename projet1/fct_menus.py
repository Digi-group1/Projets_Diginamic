import colorama

#on fait une fonction pour affiche le menu principal
def menu_principal():
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Bienvenue sur le menu principal de votre bibliothèque !")
    print("Que souhaitez-vous faire ?" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + "1 - Rechercher dans la bibliothèque")
    print("2 - Ajouter un ouvrage à la bibliothèque")
    print("3 - Supprimer un ouvrage de la bibliothèque")
    print("4 - Afficher les statistiques de la bibliothèque")
    print("5 - Quitter" + colorama.Style.RESET_ALL)
    while True :
        choix_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_input.isdigit() == True and (int(choix_input) > 0 and int(choix_input) <= 5):
            choix = int(choix_input)
            break
        else :
            print (colorama.Fore.RED + "Veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 4" + colorama.Style.RESET_ALL) 
    return choix

#On fait une fonction pour sélectionner le type de recherche dans la BDD
def menu_recherche():
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Par quel index souhaitez-vous rechercher ?" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + "1 - par auteur")
    print("2 - par titre")  
    print("3 - par année")
    print("4 - par type")
    print("5 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_recherche_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_recherche_input.isdigit() == True and (int(choix_recherche_input) > 0 and int(choix_recherche_input) <= 5):
            choix_recherche = int(choix_recherche_input)
            break
        else :
            print (colorama.Fore.RED + "Veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 5" + colorama.Style.RESET_ALL) 
    return choix_recherche

#On fait une fonction pour déterminer des options supplémentaires pour la recherche
def options_recherche() :
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Souhaitez-vous ?" + colorama.Style.RESET_ALL)    
    print(colorama.Fore.MAGENTA + "1 - Faire une recherche classique (affiche les résultats 5 par 5)")
    print("2 - Afficher plus ou moins de résultats")
    print("3 - Trier les résultats")
    print("4 - Filtrer les résultats")
    print("5 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_option_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_option_input.isdigit() == True and (int(choix_option_input) > 0 and int(choix_option_input) <= 5) :
            choix_option = int(choix_option_input)
            break
        else :
            print (colorama.Fore.RED + "Veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 5" + colorama.Style.RESET_ALL) 
    return choix_option

#On fait une fonction pour déterminer sur quelle variable on va faire le tri
def options_tri() :
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Souhaitez-vous ?" + colorama.Style.RESET_ALL)  
    print(colorama.Fore.MAGENTA + "1 - Trier par auteur")
    print("2 - Trier par titre")
    print("3 - Trier par année")
    print("4 - Trier par type")
    print("5 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_tri_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_tri_input.isdigit() == True and (int(choix_tri_input) > 0 and int(choix_tri_input) <= 5) :
            choix_tri = int(choix_tri_input)
            break
        else :
            print (colorama.Fore.RED + "Veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 5" + colorama.Style.RESET_ALL) 
    return choix_tri

#On fait une fonction pour choisir le sens du tri
def sens_tri() : 
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Souhaitez-vous trier ?" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + "1 - de manière ascendante")
    print("2 - de manière descendante")
    print("3 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_sens_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_sens_input.isdigit() == True and (int(choix_sens_input) > 0 and int(choix_sens_input) <= 3) :
            choix_sens = int(choix_sens_input)
            break
        else :
            print (colorama.Fore.RED + "Veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 3" + colorama.Style.RESET_ALL) 
    return choix_sens

#On fait une fonction pour définir le filtre à ajouter
def selection_filtre() :
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Souhaitez-vous filtrer ?" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + "1 - sur un titre en particulier")
    print("2 - sur une année en particulier")
    print("3 - sur un auteur en particulier")
    print("4 - sur un type d'ouvrage en particulier")
    print("5 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_filtre_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_filtre_input.isdigit() == True and (int(choix_filtre_input) > 0 and int(choix_filtre_input) <=5) :
            choix_filtre = int(choix_filtre_input)
            break
        else :
            print(colorama.Fore.RED + "veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 5" + colorama.Style.RESET_ALL)
    return choix_filtre

#On fait une fonction pour définir quel type d'ouvrage on ajoute
def ajout_ouvrage() :
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Souhaitez-vous ajouter ?" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + "1 - un article")
    print("2 - un livre")
    print("3 - un phd")
    print("4 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_ajout_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_ajout_input.isdigit() == True and (int(choix_ajout_input) > 0 and int(choix_ajout_input) <=3) :
            choix_ajout = int(choix_ajout_input)
            break
        else :
            print(colorama.Fore.RED + "Veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 3" + colorama.Style.RESET_ALL)
    return choix_ajout

#On fait une fonction pour définir ce que l'on veut supprimer
def suppression_ouvrage() :
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Souhaitez-vous supprimer ?" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + "1 - un seul ouvrage")
    print("2 - plusieurs ouvrages")
    print("3 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_supp_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_supp_input.isdigit() == True and (int(choix_supp_input) > 0 and int(choix_supp_input) <=3) :
            choix_supp = int(choix_supp_input)
            break
        else :
            print(colorama.Fore.RED + "Veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 3" + colorama.Style.RESET_ALL)
    return choix_supp

#On fait une fonction pour les suppressions multiples
def suppressions_multi() :
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Souhaitez-vous supprimer ?" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + "1 - une liste de plusieurs ouvrages")
    print("2 - tous les ouvrages d'un auteur en particulier")
    print("3 - tous les ouvrages d'une année en particulier")
    print("4 - tous les ouvrages d'un type en particulier")
    print("5 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_multi_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_multi_input.isdigit() == True and (int(choix_multi_input) > 0 and int(choix_multi_input) <=5) :
            choix_multi = int(choix_multi_input)
            break
        else : 
            print(colorama.Fore.RED + "Veuillez reformule votre demande - en insérant un chiffre allant de 1 à 5" + colorama.Style.RESET_ALL)
    return choix_multi

#On fait une fonction pour déterminer les statistiques à afficher
def options_stats() :
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "~~~~ Bienvenue sur la page de statistiques de votre bibliothèque ~~~~" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Souhaitez-vous afficher ?" + colorama.Style.RESET_ALL)  
    print(colorama.Fore.MAGENTA + "1 - des statistiques basiques")
    print("2 - des statistiques détaillées")
    print("3 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_stats_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_stats_input.isdigit() == True and (int(choix_stats_input) > 0 and int(choix_stats_input) <= 3) :
            choix_stats = int(choix_stats_input)
            break
        else :
            print (colorama.Fore.RED + "Veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 3" + colorama.Style.RESET_ALL) 
    return choix_stats

#On fait une fonction pour déterminer ce qu'on affiche en statistiques détaillées
def stats_detaillees_choix() :
    print(f"\n" + colorama.Fore.MAGENTA + colorama.Back.WHITE + "-------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Souhaitez-vous afficher ?" + colorama.Style.RESET_ALL)  
    print(colorama.Fore.MAGENTA + "1 - le nombre de publications par année")
    print("2 - le nombre de publications par type")
    print("3 - un TOP des auteurs les plus prolifiques")
    print("4 - un TOP des années les plus prolifiques")
    print("5 - la liste totale du nombre de publications par auteur")
    print("6 - Revenir au menu précédent" + colorama.Style.RESET_ALL)
    while True :
        choix_detaille_input = input(colorama.Fore.YELLOW + "Entrez le numéro de l'action choisie : " + colorama.Style.RESET_ALL)
        if choix_detaille_input.isdigit() == True and (int(choix_detaille_input) > 0 and int(choix_detaille_input) <= 6) :
            choix_detaille = int(choix_detaille_input)
            break
        else :
            print (colorama.Fore.RED + "Veuillez reformuler votre demande - en insérant un chiffre allant de 1 à 6" + colorama.Style.RESET_ALL) 
    return choix_detaille



    
    
