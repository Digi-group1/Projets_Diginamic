#ajouter un article à la BDD
def ajout_article(coll) :
    titre = input("Veuillez entrer le titre de l'article : ")
    annee = int(input("Veuillez entrer l'année de parution de l'article : "))
    auteur = input("Veuillez entrer le nom de l'auteur : ")
    coll.insert_one({"type":"Article","title" : titre,"year" : annee,"authors" : auteur})
    print(f"Vous venez d'ajouter l'article {titre} à votre bibliothèque")

#ajouter un livre à la BDD    
def ajout_livre(coll) :
    titre = input("Veuillez entrer le titre du livre : ")
    annee = int(input("Veuillez entrer l'année de parution du livre : "))
    auteur = input("Veuillez entrer le nom de l'auteur : ")
    coll.insert_one({"type":"Book","title" : titre,"year" : annee,"authors" : auteur})
    print(f"Vous venez d'ajouter le livre {titre} à votre bibliothèque")
    


