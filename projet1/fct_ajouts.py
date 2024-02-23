import colorama

#ajouter un article à la BDD
def ajout_article(coll) :
    titre = input(colorama.Fore.YELLOW + "Veuillez entrer le titre de l'article : " + colorama.Style.RESET_ALL).capitalize()
    annee = int(input(colorama.Fore.YELLOW + "Veuillez entrer l'année de parution de l'article : " + colorama.Style.RESET_ALL))
    auteur = input(colorama.Fore.YELLOW + "Veuillez entrer le nom de l'auteur : " + colorama.Style.RESET_ALL).title()
    coll.insert_one({"type":"Article","title" : titre,"year" : annee,"authors" : auteur})
    print(colorama.Fore.CYAN + "Vous venez d'ajouter l'article " + colorama.Fore.MAGENTA + f"{titre}" + colorama.Fore.CYAN + " à votre bibliothèque"+ colorama.Style.RESET_ALL)

#ajouter un livre à la BDD    
def ajout_livre(coll) :
    titre = input(colorama.Fore.YELLOW + "Veuillez entrer le titre du livre : " + colorama.Style.RESET_ALL).capitalize()
    annee = int(input(colorama.Fore.YELLOW + "Veuillez entrer l'année de parution du livre : " + colorama.Style.RESET_ALL))
    auteur = input(colorama.Fore.YELLOW + "Veuillez entrer le nom de l'auteur : " + colorama.Style.RESET_ALL).title()
    coll.insert_one({"type":"Book","title" : titre,"year" : annee,"authors" : auteur})
    print(colorama.Fore.CYAN + "Vous venez d'ajouter le livre " + colorama.Fore.MAGENTA + f"{titre}" + colorama.Fore.CYAN + " à votre bibliothèque"+ colorama.Style.RESET_ALL)

#ajouter un phd à la BDD :*
#ajouter un livre à la BDD    
def ajout_phd(coll) :
    titre = input(colorama.Fore.YELLOW + "Veuillez entrer le titre du phd : " + colorama.Style.RESET_ALL).capitalize()
    annee = int(input(colorama.Fore.YELLOW + "Veuillez entrer l'année de parution du phd : " + colorama.Style.RESET_ALL))
    auteur = input(colorama.Fore.YELLOW + "Veuillez entrer le nom de l'auteur : " + colorama.Style.RESET_ALL).title()
    coll.insert_one({"type":"Phd","title" : titre,"year" : annee,"authors" : auteur})
    print(colorama.Fore.CYAN + "Vous venez d'ajouter le phd " + colorama.Fore.MAGENTA + f"{titre}" + colorama.Fore.CYAN + " à votre bibliothèque"+ colorama.Style.RESET_ALL)

    