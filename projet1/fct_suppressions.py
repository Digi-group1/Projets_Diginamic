from bson.objectid import ObjectId
import colorama

#On fait une fonction pour supprimer par ID (1 seulement)
def suppression(coll) :
    index_supp = input(colorama.Fore.YELLOW + "Veuillez entrer l'id entier de l'ouvrage à supprimer : " + colorama.Style.RESET_ALL)
    if "/" in index_supp :
        coll.delete_one({"_id":index_supp})
    else :
        coll.delete_one({"_id":ObjectId(index_supp)})        
    print(colorama.Fore.CYAN + "Vous venez de supprimer l'ouvrage " + colorama.Fore.MAGENTA + f"n°{index_supp}" + colorama.Fore.CYAN + " de votre bibliothèque"+ colorama.Style.RESET_ALL)

#On fait une fonction pour déterminer le nombre d'ouvrages à supprimer en une seule fois
def pls_ouvrages():
    print("-------------------------------")
    nb_ouvrages = int(input(colorama.Fore.YELLOW + "Combien d'ouvrages souhaitez-vous supprimer ? " + colorama.Style.RESET_ALL))
    return nb_ouvrages

#On fait une fonction pour supprimer plusieurs ouvrages par ID
def suppression_multiple(coll,nb_ouvrages) : 
    table_supp = []
    for i in range(nb_ouvrages) :
        if i == 0 : 
            index_supp = input(colorama.Fore.YELLOW + "Veuillez entrer l'id entier du 1er ouvrage : " + colorama.Style.RESET_ALL)
            if "/" in index_supp :
                table_supp.append(index_supp)
            else :
                table_supp.append(ObjectId(index_supp))
        else:
            index_supp = input(colorama.Fore.YELLOW + f"Veuillez entrer l'id entier du {i+1}ème ouvrage : " + colorama.Style.RESET_ALL)
            if "/" in index_supp :
                table_supp.append(index_supp)
            else :
                table_supp.append(ObjectId(index_supp))
    coll.delete_many({"_id":table_supp})
    print(colorama.Fore.CYAN + "Vous venez de supprimer " + colorama.Fore.MAGENTA + f"{nb_ouvrages}" + colorama.Fore.CYAN + " de votre bibliothèque"+ colorama.Style.RESET_ALL)


#On fait une fonction pour supprimer tous les ouvrages d'un auteur    
def suppression_auteur(coll) :
    while True :
        auteur_sup_input = input(colorama.Fore.YELLOW + "Veuillez entrer les prénom et nom de l'auteur : " + colorama.Style.RESET_ALL).title()
        if not auteur_sup_input.isdigit() :
            auteur_sup = auteur_sup_input
            if auteur_sup in coll.distinct("authors") : 
                coll.delete_many({"authors":auteur_sup})
                print(colorama.Fore.CYAN + "Vous venez de supprimer tous les ouvrages écrits par " + colorama.Fore.MAGENTA + f"{auteur_sup}" + colorama.Fore.CYAN + " uniquement"+ colorama.Style.RESET_ALL)
                break
            else : 
                print(f"Veuillez reformuler votre demande - en insérant bien le prénom et le nom de l'auteur")
        else : 
            print("Veuillez reformuler votre demande - L'auteur ne doit pas comporter de caractères spéciaux, que des lettres")
                

#On fait une fonction pour supprimer tous les ouvrages d'une année    
def suppression_annee(coll) :
    while True : 
        annee_sup_input = input(colorama.Fore.YELLOW + "Veuillez entrer l'année : " + colorama.Style.RESET_ALL)
        if annee_sup_input.isdigit() and len(annee_sup_input) == 4 :
            annee_sup = int(annee_sup_input)
            coll.delete_many({"year":annee_sup})
            print(f"Vous venez de supprimer tous les ouvrages parus en {annee_sup}")
            print(colorama.Fore.CYAN + "Vous venez de supprimer tous les ouvrages parus en " + colorama.Fore.MAGENTA + f"{annee_sup}" + colorama.Style.RESET_ALL)
            break
        else :
            print("Veuillez reformuler votre demande - L'année doit comporter 4 chiffres")

#On fait une fonction pour supprimer tous les ouvrages d'un certain type
def suppression_type(coll) :
    while True :
        type_sup_input = input(colorama.Fore.YELLOW + "Entrez le type à supprimer (livre, article ou phd) : " + colorama.Style.RESET_ALL)
        if type_sup_input.lower() == "livre" :
            type_sup = "Book"
        elif type_sup_input.lower() == "article" :
            type_sup = "Article"
        elif type_sup_input.lower() == "phd" :
            type_sup = "Phd" 
        else :
            print("Veuillez reformuler votre demande - en inscrivant livre, article ou phd")
        coll.delete_many({"type":type_sup})
        print(colorama.Fore.CYAN + "Vous venez de supprimer tous les " + colorama.Fore.MAGENTA + f"{type_sup_input.lower()}" + colorama.Fore.CYAN + " de votre bibliothèque"+ colorama.Style.RESET_ALL)
        break
        
        

        
        
    