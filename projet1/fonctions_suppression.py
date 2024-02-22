from bson.objectid import ObjectId

#suppression par ID
def suppression(coll) :
    index_supp = input("Veuillez entrer l'id entier de l'ouvrage à supprimer : ")
    coll.delete_one({"_id":ObjectId(index_supp)})
    print(f"Vous venez de supprimer l'ouvrage n°{index_supp} de votre bibliothèque")

#suppression de plusieurs ouvrages par ID
def suppression_multiple(coll,nb_ouvrages) : 
    table_supp = []
    for i in range(nb_ouvrages) :
        if i == 0 : 
            index_supp = input("Veuillez entrer l'id entier du 1er ouvrage : ")
            table_supp.append(index_supp)
        else:
            index_supp = input(f"Veuillez entrer l'id entier du {i+1}ème ouvrage :")
            table_supp.append(index_supp)
    coll.delete_many({"_id":ObjectId(table_supp)})
    print(f"Vous venez de supprimer {nb_ouvrages} ouvrages de votre bibliothèque")

#suppression de tous les ouvrages d'un auteur    
def suppression_auteur(coll) :
    auteur_sup = input("Veuillez entrer les prénom et nom de l'auteur : ")
    coll.delete_many({"authors":auteur_sup})
    print(f"Vous venez de supprimer tous les ouvrages écrtis par {auteur_sup} uniquement")

#suppression de tous les ouvrages d'une année    
def suppression_annee(coll) :
    annee_sup = int(input("Veuillez entrer l'année : "))
    coll.delete_many({"year":annee_sup})
    print(f"Vous venez de supprimer tous les ouvrages parus en {annee_sup}")
        
        
    